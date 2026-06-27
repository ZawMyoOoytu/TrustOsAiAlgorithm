class ToolRouter:

    def route(self, node_output: dict):

        # Example expected format:
        # {
        #   "action": "tool",
        #   "name": "draw_website",
        #   "input": {}
        # }

        if isinstance(node_output, dict) and node_output.get("action") == "tool":

            return {
                "tool_name": node_output["name"],
                "input": node_output.get("input", {})
            }

        return None