from backend.engine.planner import Planner

from backend.agents.reasoning_agent import ReasoningAgent
from backend.agents.summarizer_agent import SummarizerAgent


class Executor:

    def __init__(self):

        self.planner = Planner()

        self.reasoning = ReasoningAgent()

        self.summarizer = SummarizerAgent()

    def execute(self, task):

        plan = self.planner.create_plan(task)

        result = task

        for step in plan:

            if step == "reasoning":

                result = self.reasoning.run(result)

            elif step == "summarizer":

                result = self.summarizer.run(
                    result["output"]
                )

        return result