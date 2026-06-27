from fastapi import APIRouter
from backend.db.sqlite_db import get_all_executions

router = APIRouter()


@router.get("/policy/stats")
def policy_stats():

    executions = get_all_executions()

    allowed = 0
    blocked = 0
    low_risk = 0
    high_risk = 0

    for e in executions:

        trust = e.get("trust_score", 0)
        result = e.get("result", {})

        # blocked detection (fallback logic)
        if result.get("status") == "blocked":
            blocked += 1
        else:
            allowed += 1

        # risk classification
        if trust >= 70:
            high_risk += 1
        else:
            low_risk += 1

    return {
        "total": len(executions),
        "allowed": allowed,
        "blocked": blocked,
        "low_risk": low_risk,
        "high_risk": high_risk,
        "engine": "active"
    }