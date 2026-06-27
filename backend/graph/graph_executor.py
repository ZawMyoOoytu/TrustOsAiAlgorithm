class GraphExecutor:

    def __init__(self, tool_executor, llm_func):
        self.tool_executor = tool_executor
        self.llm_func = llm_func

    def execute(self, graph: dict):

        context = {}
        trace = []

        current_node_id = "start"

        while current_node_id:

            node = graph[current_node_id]

            trace.append({
                "node": current_node_id,
                "action": node["action"]
            })

            action = node["action"]

            # =========================
            # ACTION ROUTING
            # =========================

            if action == "analyze_task":
                context["task"] = node["data"]["task"]

            elif action == "llm_plan":
                prompt = f"Plan this task: {context.get('task')}"
                context["plan"] = self.llm_func(prompt)

            elif action == "tool_or_llm":

                # simple decision logic (upgrade later)
                if "draw" in context.get("task", ""):
                    context["result"] = self.tool_executor.execute(
                        "draw_website",
                        {}
                    )
                else:
                    context["result"] = self.llm_func(context.get("task"))

            elif action == "format_output":
                context["final"] = {
                    "task": context.get("task"),
                    "plan": context.get("plan"),
                    "result": context.get("result")
                }

            # =========================
            # MOVE NEXT
            # =========================

            next_nodes = node.get("next_nodes", [])
            current_node_id = next_nodes[0] if next_nodes else None

        return {
            "state": "FINISHED",
            "trace": trace,
            "output": context.get("final")
        }