from backend.engine.intent_engine import classify_intent

def route_execution(intent: str) -> str:
    """
    Decide how system should execute task
    """

    if intent == "design_request":
        return "structured_design"

    if intent == "website_generation":
        return "code_generation"

    if intent == "knowledge_query":
        return "normal_llm"

    if intent == "risky_task":
        return "blocked"

    return "normal_llm"