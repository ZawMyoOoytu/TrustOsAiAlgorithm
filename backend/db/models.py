from dataclasses import dataclass

@dataclass
class Execution:
    execution_id: str
    task: str
    status: str
    result: str