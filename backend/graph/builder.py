from backend.llm.planner import llm_plan


def build_graph(task: str):
    plan = llm_plan(task)

    return plan["nodes"], plan["reasoning"]