from pydantic import BaseModel
from typing import Any, Dict, List, Optional


class ExecutionResult(BaseModel):
    execution_id: str
    status: str
    trust_score: float
    policy: Dict[str, Any]

    execution_state: str

    tool_calls: Optional[List[Dict[str, Any]]] = []

    graph_trace: Optional[List[Dict[str, Any]]] = []

    result: Any