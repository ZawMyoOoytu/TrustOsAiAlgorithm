class GraphBuilder:

    def build(self, task: str):
        """
        Converts task into execution nodes
        """

        return [
            {
                "id": "intent",
                "type": "analyze",
                "input": task
            },
            {
                "id": "structure",
                "type": "transform",
                "input_from": "intent"
            },
            {
                "id": "finalize",
                "type": "format_json",
                "input_from": "structure"
            }
        ]