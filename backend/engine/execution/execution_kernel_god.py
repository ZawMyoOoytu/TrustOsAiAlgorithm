from backend.engine.agents.planner_agent import PlannerAgent
from backend.engine.agents.executor_agent import ExecutorAgent
from backend.engine.agents.validator_agent import ValidatorAgent
from backend.engine.agents.memory_agent import MemoryAgent


class ExecutionKernelGod:

    def __init__(self, llm, tool_executor):

        self.planner = PlannerAgent(llm)
        self.executor = ExecutorAgent(tool_executor, llm)
        self.validator = ValidatorAgent()
        self.memory = MemoryAgent()

    # =========================
    # MAIN GOD LOOP
    # =========================
    def run(self, task: str):

        # =====================
        # 1. INITIAL PLAN
        # =====================
        plan = self.planner.run(task)

        steps = self._parse_plan(plan)

        results = []

        # =====================
        # 2. EXECUTION LOOP
        # =====================
        for i, step in enumerate(steps):

            raw_result = self.executor.run(step)

            validated = self.validator.run(raw_result)

            # =====================
            # MEMORY UPDATE
            # =====================
            self.memory.write({
                "step": step,
                "result": validated
            })

            results.append(validated)

            # =====================
            # SELF REASONING LOOP
            # =====================
            if not validated.get("valid", True):

                # REPLAN if failure happens
                new_plan = self.planner.run(
                    f"Fix this step: {step}"
                )

                steps.extend(self._parse_plan(new_plan))

        # =====================
        # FINAL OUTPUT
        # =====================
        return {
            "status": "completed",
            "task": task,
            "plan": plan,
            "results": results,
            "memory": self.memory.read()
        }

    # =========================
    # PLAN PARSER (SIMPLE v1)
    # =========================
    def _parse_plan(self, plan: str):

        """
        Convert LLM plan → structured steps
        (v1 simple parser, later upgrade to JSON planner)
        """

        lines = plan.split("\n")

        steps = []

        for line in lines:
            if "tool" in line.lower():
                steps.append({
                    "action": "tool",
                    "name": "draw_website",
                    "input": {}
                })
            else:
                steps.append({
                    "action": "llm",
                    "input": line
                })

        return steps
        from backend.engine.execution.parallel_executor import ParallelExecutor


class ExecutionKernelGod:

    def __init__(self, llm, tool_executor):

        self.planner = PlannerAgent(llm)
        self.executor = ExecutorAgent(tool_executor, llm)
        self.validator = ValidatorAgent()
        self.memory = MemoryAgent()

        # 🔥 NEW
        self.parallel = ParallelExecutor(
            self.executor,
            self.validator,
            self.memory
        )

    def run(self, task: str):

        plan = self.planner.run(task)
        steps = self._parse_plan(plan)

        # =========================
        # 🔥 PARALLEL EXECUTION
        # =========================
        result = self.parallel.run(steps)

        return {
            "status": "completed_god_parallel",
            "task": task,
            "plan": plan,
            "result": result,
            "memory": self.memory.read()
        }