def calculate_trust(policy):

    score = 100

    score -= policy["risk_score"]

    if score < 0:
        score = 0

    return score