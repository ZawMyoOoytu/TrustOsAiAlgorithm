from backend.tools.calculator import CalculatorTool

TOOL_REGISTRY = {
    "calculator": CalculatorTool()
}


def get_tool(name: str):
    return TOOL_REGISTRY.get(name)