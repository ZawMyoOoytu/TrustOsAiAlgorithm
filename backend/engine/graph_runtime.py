class GraphRuntime:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, name, fn):
        self.nodes[name] = fn
        self.edges[name] = []

    def add_edge(self, frm, to):
        self.edges[frm].append(to)

    def execute(self, start_node, data):
        visited = set()
        return self._run(start_node, data, visited)

    def _run(self, node, data, visited):
        if node in visited:
            return data

        visited.add(node)

        result = self.nodes[node](data)

        for child in self.edges[node]:
            result = self._run(child, result, visited)

        return result