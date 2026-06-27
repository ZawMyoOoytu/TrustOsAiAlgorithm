from backend.engine.distributed.redis_queue import RedisQueue
from backend.engine.distributed.node_registry import NodeRegistry


class Dispatcher:

    def __init__(self):

        self.queue = RedisQueue()
        self.registry = NodeRegistry()

    # =========================
    # SEND TASK
    # =========================
    def dispatch(self, task: dict):

        nodes = self.registry.get_nodes()

        # simple round-robin / first node (v1)
        target_node = list(nodes.keys())[0] if nodes else None

        if not target_node:
            raise Exception("No worker nodes available")

        task["target"] = target_node

        self.queue.push("tasks", task)

        return {
            "status": "dispatched",
            "node": target_node
        }

    # =========================
    # COLLECT RESULT
    # =========================
    def collect(self):

        return self.queue.pop("results")