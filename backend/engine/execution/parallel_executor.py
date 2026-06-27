import asyncio
from concurrent.futures import ThreadPoolExecutor


class ParallelExecutor:

    def __init__(self, executor_agent, validator_agent, memory_agent):
        self.executor = executor_agent
        self.validator = validator_agent
        self.memory = memory_agent

        self.pool = ThreadPoolExecutor(max_workers=5)

    # =========================
    # MAIN ENTRY
    # =========================
    def run(self, steps: list):

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        tasks = [
            self._run_step(step)
            for step in steps
        ]

        results = loop.run_until_complete(
            asyncio.gather(*tasks)
        )

        return {
            "status": "completed_parallel",
            "results": results
        }

    # =========================
    # SINGLE STEP EXECUTION
    # =========================
    async def _run_step(self, step: dict):

        loop = asyncio.get_event_loop()

        # run executor in thread pool (simulate async tool/llm)
        raw_result = await loop.run_in_executor(
            self.pool,
            self.executor.run,
            step
        )

        validated = self.validator.run(raw_result)

        self.memory.write({
            "step": step,
            "result": validated
        })

        return validated