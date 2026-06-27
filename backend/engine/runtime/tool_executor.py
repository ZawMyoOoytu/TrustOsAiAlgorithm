class ToolExecutor:

    def __init__(self, registry):
        self.registry = registry

    def execute(self, tool_name: str, input_data: dict):

        tool = self.registry.get(tool_name)

        if not tool:
            return {
                "error": f"Tool not found: {tool_name}"
            }

        return tool(input_data)