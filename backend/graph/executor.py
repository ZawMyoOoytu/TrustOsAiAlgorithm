from backend.tools.registry import get_tool


def execute_graph(nodes):
    context = {}

    for node in nodes:

        if node["type"] == "tool":
            tool = get_tool(node["tool"])

            if tool:
                result = tool.run(node["action"], node["input"])
                node["output"] = result
                context[node["tool"]] = result

        elif node["type"] == "final":
            context["final"] = node.get("output")

    return context, nodes