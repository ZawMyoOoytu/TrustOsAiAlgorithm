from backend.core.llm_brain import LLMBrian


class AgentEngine:
    def __init__(self):
        self.brain = LLMBrian()

    def run(self, task: str):
        # 1. LLM thinking
        brain_output = self.brain.think(task)

        reasoning = brain_output["reasoning"]
        plan = brain_output["plan"]

        # 2. tool execution
        tool_result = self._execute_tool(task, plan)

        # 3. final output
        return {
            "task": task,
            "reasoning": reasoning,
            "plan": plan,
            "tool_result": tool_result,
            "output": self._finalize(task, plan, tool_result),
        }

    def _execute_tool(self, task, plan):
        if plan.get("tool") == "calculator":
            return {
                "tool": "calculator",
                "result": self._fake_calc(task),
            }

        return {
            "tool": "none",
            "result": "no tool executed",
        }

    def _fake_calc(self, task):
        # simple demo logic
        if "+" in task:
            try:
                parts = task.split("+")
                return int(parts[0].strip()) + int(parts[1].strip())
            except:
                return 0
        return 0

    def _finalize(self, task, plan, tool_result):
        return f"Task '{task}' executed with plan={plan.get('type')} and tool={tool_result['tool']}"