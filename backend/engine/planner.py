class Planner:

    def create_plan(self, task: str):

        task = task.lower()

        if "summarize" in task:
            return [
                "reasoning",
                "summarizer"
            ]

        return [
            "reasoning"
        ]