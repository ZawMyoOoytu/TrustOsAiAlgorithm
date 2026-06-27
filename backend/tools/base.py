from typing import Dict, Any


class Tool:
    name: str = "base"

    def run(self, action: str, input_data: Any):
        raise NotImplementedError