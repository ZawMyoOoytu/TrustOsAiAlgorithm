from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class PolicyResult:
    risk_level: str
    risk_score: int
    flags: List[str]
    action: str
    reason: str
    trust_score_delta: int


class PolicyEngine:

    def evaluate(self, task: str) -> PolicyResult:
        flags = []
        risk_score = 0
        action = "allow"
        reason = "safe execution"
        trust_delta = 0

        task_lower = task.lower()

        # simple rule system (upgrade later to ML/rules file)
        if "phishing" in task_lower or "login" in task_lower:
            flags.append("suspicious_auth")
            risk_score += 30
            trust_delta -= 40

        if "hack" in task_lower:
            flags.append("malicious_intent")
            risk_score += 60
            trust_delta -= 80
            action = "block"
            reason = "high-risk malicious intent detected"

        if risk_score >= 70:
            action = "block"
            reason = "high risk execution blocked"
        elif risk_score >= 30:
            action = "sandbox"
            reason = "medium risk → sandbox execution"
        else:
            action = "allow"

        risk_level = (
            "high" if risk_score >= 70 else
            "medium" if risk_score >= 30 else
            "low"
        )

        return PolicyResult(
            risk_level=risk_level,
            risk_score=risk_score,
            flags=flags,
            action=action,
            reason=reason,
            trust_score_delta=trust_delta
        )