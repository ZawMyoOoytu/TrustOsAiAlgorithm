from backend.engine.runtime.tool_registry import ToolRegistry
from backend.engine.runtime.tool_executor import ToolExecutor
from backend.engine.runtime.tool_router import ToolRouter
from backend.engine.output_state_machine import OutputStateMachine
from backend.engine.execution.execution_context import ExecutionContext
from backend.engine.execution.execution_types import ExecutionResult

import uuid


class ExecutionKernel:

    def __init__(self, llm_func, compiler):
        self.llm_call_func = llm_func
        self.compiler = compiler

        self.registry = ToolRegistry()
        self.executor = ToolExecutor(self.registry)
        self.router = ToolRouter()
        self.state_machine = OutputStateMachine()

    # =========================
    # MAIN RUN
    # =========================
    def run(self, task: str, contract: dict, intent: str, trust: float, policy: dict):

        execution_id = str(uuid.uuid4())
        context = ExecutionContext(execution_id)

        # =========================
        # 1. PROMPT COMPILATION
        # =========================
        prompt = self.compiler.compile(
            task=task,
            contract=contract,
            mode=contract.get("mode", "normal")
        )

        # =========================
        # 2. LLM CALL
        # =========================
        raw_output = self.llm_call_func(prompt)

        # =========================
        # 3. TOOL ROUTING (HARD CHECK)
        # =========================
        tool_call = self.router.route(raw_output)

        if tool_call:
            context.set_state("TOOL_EXEC")

            result = self.executor.execute(
                tool_call["tool_name"],
                tool_call["input"]
            )

            context.add_tool_call(tool_call)

        else:
            result = raw_output
            context.set_state("LLM_ONLY")

        # =========================
        # 4. STATE MACHINE ENFORCEMENT
        # =========================
        final = self.state_machine.enforce(
            mode=contract.get("mode", "normal"),
            raw_output=result
        )

        context.set_state(final.get("state", "UNKNOWN"))

        # =========================
        # 5. FINAL OUTPUT (UI READY)
        # =========================
        return ExecutionResult(
            execution_id=execution_id,
            status="completed",
            trust_score=trust,
            policy=policy,

            execution_state=context.state,

            tool_calls=context.tool_calls,
            graph_trace=context.graph_trace,

            result=final
        ).dict()