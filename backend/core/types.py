from pydantic import BaseModel
from typing import Dict, Any

class TaskRequest(BaseModel):
    task: str
    mode: str = "balanced"
    max_cost: float = 0
    allow_reasoning: bool = True
    metadata: Dict[str, Any] = {}