from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    id: str
    type: str          # "tool" | "llm" | "transform"
    tool: Optional[str]
    action: Optional[str]
    input: Any
    output: Any = None