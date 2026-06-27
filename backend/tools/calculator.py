from backend.tools.base import Tool


class CalculatorTool(Tool):
    name = "calculator"

    def run(self, action: str, input_data: str):
        try:
            if action == "add":
                parts = input_data.split("+")
                return int(parts[0]) + int(parts[1])

            return None
        except:
            return None