class ExecutionKernelV2:

    def __init__(self, llm, tool_executor):
        self.llm = llm
        self.tool_executor = tool_executor

        self.planner = PlannerAgent(llm)
        self.executor = ExecutorAgent(tool_executor, llm)
        self.validator = ValidatorAgent()
        self.memory = MemoryAgent()

    def run(self, task: str):

        # =====================
        # 1. PLAN
        # =====================
        plan = self.planner.run(task)

        # =====================
        # 2. EXECUTE (simple loop v1)
        # =====================
        result = self.executor.run({
            "action": "llm",
            "input": plan
        })

        # =====================
        # 3. VALIDATE
        # =====================
        validated = self.validator.run(result)

        # =====================
        # 4. MEMORY
        # =====================
        self.memory.write({
            "task": task,
            "result": validated
        })

        # =====================
        # 5. RETURN
        # =====================
        return {
            "status": "completed",
            "task": task,
            "plan": plan,
            "result": validated,
            "memory": self.memory.read()
        }