from typing import Literal

IntentType = Literal[
    "design_request",
    "website_generation",
    "knowledge_query",
    "general_task",
    "risky_task"
]


def classify_intent(task: str) -> IntentType:
    """
    Simple rule-based intent classifier
    (upgrade later to ML model if needed)
    """

    text = task.lower()

    # 🚨 risky intent
    risky_keywords = ["hack", "phishing", "steal", "exploit"]
    if any(word in text for word in risky_keywords):
        return "risky_task"

    # 🎨 UI / design related
    if any(word in text for word in ["draw", "design", "ui", "wireframe"]):
        return "design_request"

    # 🌐 website generation
    if "website" in text and any(word in text for word in ["create", "build", "make"]):
        return "website_generation"

    # 📚 knowledge queries
    if any(word in text for word in ["what is", "explain", "how", "why"]):
        return "knowledge_query"

    return "general_task"