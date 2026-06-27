class PlannerAgent:

    def __init__(self, llm):
        self.llm = llm

    def run(self, task: str):

        prompt = f"""
You are a planner agent.

Break this task into steps:
TASK: {task}

Return structured plan.
"""

        return self.llm(prompt)