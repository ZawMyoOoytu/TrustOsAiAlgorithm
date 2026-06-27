class GraphBuilder:

    def build(self, task: str):
        """
        Simple deterministic graph builder (v1)
        later upgrade → LLM-based planner graph
        """

        return {
            "start": {
                "node_id": "start",
                "action": "analyze_task",
                "data": {"task": task},
                "next_nodes": ["plan"]
            },

            "plan": {
                "node_id": "plan",
                "action": "llm_plan",
                "data": {},
                "next_nodes": ["execute"]
            },

            "execute": {
                "node_id": "execute",
                "action": "tool_or_llm",
                "data": {},
                "next_nodes": ["finalize"]
            },

            "finalize": {
                "node_id": "finalize",
                "action": "format_output",
                "data": {},
                "next_nodes": []
            }
        }