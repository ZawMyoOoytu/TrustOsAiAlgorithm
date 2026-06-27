def calculate_trust(policy_result):
    trust_score = 100 - policy_result["risk_score"]

    if trust_score < 0:
        trust_score = 0

    return trust_score