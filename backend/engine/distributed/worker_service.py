from backend.engine.distributed.redis_queue import RedisQueue


class WorkerService:

    def __init__(self, node_id, executor, validator):

        self.node_id = node_id
        self.queue = RedisQueue()

        self.executor = executor
        self.validator = validator

    # =========================
    # MAIN LOOP
    # =========================
    def run(self):

        while True:

            task = self.queue.pop("tasks")

            if not task:
                continue

            if task.get("target") != self.node_id:
                continue

            raw = self.executor.run(task)

            result = self.validator.run(raw)

            self.queue.push("results", {
                "node": self.node_id,
                "result": result
            })