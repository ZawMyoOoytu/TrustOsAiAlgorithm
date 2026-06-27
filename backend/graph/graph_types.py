from typing import List, Dict, Any, Optional


class GraphNode:
    def __init__(self, node_id: str, action: str, data: Dict[str, Any], next_nodes: Optional[List[str]] = None):
        self.node_id = node_id
        self.action = action
        self.data = data
        self.next_nodes = next_nodes or []


class ExecutionGraph:
    def __init__(self, nodes: Dict[str, GraphNode]):
        self.nodes = nodes
        self.start_node = "start"