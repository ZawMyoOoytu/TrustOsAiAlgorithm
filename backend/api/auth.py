from fastapi import APIRouter
from pydantic import BaseModel
import uuid

router = APIRouter()

USERS_DB = {}


class User(BaseModel):
    email: str
    password: str


@router.post("/register")
def register(user: User):

    user_id = str(uuid.uuid4())

    USERS_DB[user_id] = {
        "email": user.email,
        "password": user.password,
        "credits": 100,   # 🔥 free trial credits
    }

    return {"user_id": user_id, "credits": 100}