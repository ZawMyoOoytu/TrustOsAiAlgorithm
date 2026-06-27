def enforce_policy(user_id, prompt):

    risk = 0

    if "hack" in prompt:
        risk += 90

    if "exploit" in prompt:
        risk += 90

    if len(prompt) > 3000:
        risk += 30

    allowed = risk < 70

    return {
        "allowed": allowed,
        "risk_score": risk,
        "reason": "OK" if allowed else "HIGH_RISK"
    }