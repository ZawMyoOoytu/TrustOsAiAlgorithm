class NodeExecutor:

    def execute(self, node, context, llm_func):

        if node["type"] == "analyze":
            return {
                "intent": "website_layout"
            }

        if node["type"] == "transform":
            return {
                "type": "website_layout",
                "data": {
                    "header": True,
                    "body": True,
                    "footer": True
                }
            }

        if node["type"] == "format_json":
            return context.get("structure")

        return {}