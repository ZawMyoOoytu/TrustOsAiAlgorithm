from fastapi import APIRouter, HTTPException, Query
from backend.db.sqlite_db import (
    get_execution,
    get_all_executions,
    execution_count
)

router = APIRouter(tags=["Executions"])


# =========================
# GET ALL EXECUTIONS
# =========================
@router.get("/executions")
def get_all(limit: int = Query(50, ge=1, le=1000)):
    data = get_all_executions()

    # latest first + limit
    data = list(reversed(data))[:limit]

    return {
        "status": "success",
        "total": len(data),
        "executions": data
    }


# =========================
# GET SINGLE EXECUTION
# =========================
@router.get("/executions/{execution_id}")
def get_one(execution_id: str):

    execution = get_execution(execution_id)

    if not execution:
        raise HTTPException(
            status_code=404,
            detail="Execution not found"
        )

    return {
        "status": "success",
        "execution": execution
    }


# =========================
# STATS
# =========================
@router.get("/stats")
def get_stats():

    total = execution_count()

    executions = get_all_executions()

    success_count = len([
        e for e in executions if e.get("status") == "completed"
    ])

    failed_count = total - success_count

    return {
        "status": "success",
        "stats": {
            "total": total,
            "completed": success_count,
            "failed": failed_count
        }
    }