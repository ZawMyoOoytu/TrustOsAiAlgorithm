class NodeRegistry:

    def __init__(self):
        self.nodes = {}

    def register(self, node_id, meta):
        self.nodes[node_id] = {
            "status": "active",
            "meta": meta
        }

    def get_nodes(self):
        return self.nodes

    def heartbeat(self, node_id):
        if node_id in self.nodes:
            self.nodes[node_id]["status"] = "alive"