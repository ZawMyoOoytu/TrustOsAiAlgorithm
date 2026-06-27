class ExecutionContext:

    def __init__(self, execution_id: str):
        self.execution_id = execution_id
        self.state = "INIT"
        self.tool_calls = []
        self.graph_trace = []

    def add_tool_call(self, call):
        self.tool_calls.append(call)

    def add_trace(self, node):
        self.graph_trace.append(node)

    def set_state(self, state: str):
        self.state = state