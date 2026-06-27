def calculate_trust_score(
    allowed: bool,
    risk: str,
    estimated_cost: float,
):
    score = 100

    if not allowed:
        score = 0

    if risk == "medium":
        score -= 20

    if risk == "high":
        score -= 50

    if estimated_cost > 0.3:
        score -= 10

    return max(score, 0)