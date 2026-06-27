def evaluate_policy(task: str):
    task_lower = task.lower()

    risk_score = 0
    flags = []

    risky_keywords = [
        "hack",
        "exploit",
        "malware",
        "crypto trading",
        "ddos",
        "bypass",
        "phishing",
        "steal"
    ]

    for keyword in risky_keywords:
        if keyword in task_lower:
            risk_score += 20
            flags.append(keyword)

    if risk_score >= 60:
        level = "high"
    elif risk_score >= 20:
        level = "medium"
    else:
        level = "low"

    return {
        "risk_score": risk_score,
        "risk_level": level,
        "flags": flags
    }