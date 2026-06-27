from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from backend.engine.run_execution import run_execution

router = APIRouter(
    prefix="/agent",
    tags=["Agent Execution"]
)

# =========================
# REQUEST MODEL
# =========================
class RunRequest(BaseModel):
    user_id: Optional[str] = "anonymous"
    task: str
    metadata: Optional[dict] = None


# =========================
# MAIN EXECUTION ENDPOINT
# =========================
@router.post("/run")
async def run_agent(req: RunRequest):
    """
    Main AI execution endpoint
    Flow:
    API → Controller → Billing → Policy → Execution Engine
    """

    try:
        result = await run_execution(
            task=req.task,
            user_id=req.user_id or "anonymous",
            metadata=req.metadata or {}
        )

        return {
            "status": "success",
            "data": result
        }

    except Exception as e:
        # IMPORTANT: never crash frontend
        return {
            "status": "error",
            "message": str(e)
        }