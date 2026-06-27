from backend.engine.execution.event_bus import EventBus
from backend.engine.execution.execution_queue import ExecutionQueue
from backend.engine.execution.worker_node import WorkerNode


class ExecutionKernelFinal:

    def __init__(self, executor, validator, memory):

        self.bus = EventBus()
        self.queue = ExecutionQueue()

        self.worker = WorkerNode(executor, validator, memory)
        self.memory = memory

        # subscribe worker to event
        self.bus.subscribe("task", self._on_task)

    # =========================
    # ENTRY POINT
    # =========================
    def run(self, task: str):

        self.bus.publish("task", task)

        results = []

        while not self.queue.empty():

            job = self.queue.pop()
            result = self.worker.process(job)

            results.append(result)

        return {
            "status": "completed_final_kernel",
            "result": results,
            "memory": self.memory.read()
        }

    # =========================
    # EVENT HANDLER
    # =========================
    def _on_task(self, task):

        # split task into execution units
        steps = self._split(task)

        for s in steps:
            self.queue.push(s)

    # =========================
    # SIMPLE SPLITTER
    # =========================
    def _split(self, task):

        return [
            {"action": "analyze", "input": task},
            {"action": "execute", "input": task},
            {"action": "validate", "input": task}
        ]