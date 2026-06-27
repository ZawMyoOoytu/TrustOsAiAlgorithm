from dataclasses import dataclass, field

@dataclass
class ExecutionContext:
    execution_id: str
    task: str

    status: str = "pending"

    total_cost: float = 0.0

    steps: list = field(default_factory=list)

    metadata: dict = field(default_factory=dict)