import os


class LLMBrian:
    """
    LLM Brain Layer (OpenAI-ready, fallback mode included)
    """

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")

    def think(self, task: str) -> dict:
        """
        Simulated LLM reasoning (replace with real API later)
        """

        # ---- MOCK LLM RESPONSE (safe default) ----
        reasoning = f"""
I am analyzing the task: {task}

Step 1: Understand intent
Step 2: Identify if tools are needed
Step 3: Generate structured plan
"""

        plan = self._generate_plan(task)

        return {
            "reasoning": reasoning.strip(),
            "plan": plan,
        }

    def _generate_plan(self, task: str):
        task_lower = task.lower()

        if "sum" in task_lower or "+" in task_lower:
            return {
                "type": "tool_call",
                "tool": "calculator",
                "action": "add",
            }

        return {
            "type": "direct_answer",
            "tool": None,
        }