class ExecutorAgent:

    def __init__(self, tool_executor, llm):
        self.tool_executor = tool_executor
        self.llm = llm

    def run(self, step: dict):

        action = step.get("action")

        if action == "tool":
            return self.tool_executor.execute(
                step["name"],
                step.get("input", {})
            )

        return self.llm(step.get("input", ""))