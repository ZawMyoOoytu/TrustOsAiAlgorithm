from fastapi import APIRouter
from backend.memory.memory import get_memory

router = APIRouter()


@router.get("/memory/{user_id}")
def user_memory(user_id: str):
    return {
        "user_id": user_id,
        "memory": get_memory(user_id)
    }