BLOCKED_WORDS = [
    "hack bank",
    "steal password",
    "malware",
    "ransomware"
]

def evaluate_policy(task: str):

    for word in BLOCKED_WORDS:

        if word.lower() in task.lower():

            return {
                "allow": False,
                "risk_level": "high",
                "risk_score": 90,
                "action": "block",
                "reason": f"Matched blocked phrase: {word}"
            }

    return {
        "allow": True,
        "risk_level": "low",
        "risk_score": 0,
        "action": "allow",
        "reason": "allowed execution"
    }