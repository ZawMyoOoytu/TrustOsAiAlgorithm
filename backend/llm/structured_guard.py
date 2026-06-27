from typing import Dict, Any

class StructuredModeGuard:
    """
    Prevents LLM from interpreting task when structured mode is active.
    Forces schema mapping only.
    """

    def __init__(self):
        pass

    def build_structured_prompt(self, task: str, schema: Dict[str, Any], mode: str) -> str:

        # 🔥 CRITICAL RULE ENFORCEMENT
        if mode == "structured":

            return f"""
You are NOT an assistant.
You are ONLY a schema mapper.

🚨 RULES (HARD ENFORCED):
- DO NOT interpret the task
- DO NOT explain
- DO NOT ask questions
- DO NOT add opinions
- DO NOT generate extra content
- ONLY map input into schema format

TASK:
{task}

SCHEMA TO FOLLOW:
{schema}

OUTPUT:
Return ONLY valid JSON matching schema exactly.
"""

        # normal mode fallback
        return f"""
TASK:
{task}

Return structured response if possible.
"""