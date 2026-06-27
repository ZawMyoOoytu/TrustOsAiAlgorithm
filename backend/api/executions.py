from fastapi import APIRouter
from backend.db.sqlite_db import get_execution, get_all_executions

router = APIRouter()

@router.get("/executions")
def list_exec():
    return get_all_executions()


@router.get("/executions/{execution_id}")
def get_exec(execution_id: str):
    return get_execution(execution_id)