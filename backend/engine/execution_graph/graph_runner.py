from backend.engine.execution_graph.graph_builder import GraphBuilder
from backend.engine.execution_graph.node_executor import NodeExecutor

class GraphRunner:

    def __init__(self):
        self.builder = GraphBuilder()
        self.executor = NodeExecutor()

    def run(self, task, llm_func=None):

        graph = self.builder.build(task)

        context = {}

        for node in graph:
            result = self.executor.execute(node, context, llm_func)
            context[node["id"]] = result

        return {
            "status": "completed",
            "graph": graph,
            "result": context.get("finalize")
        }