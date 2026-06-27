class ValidatorAgent:

    def run(self, output):

        # simple rule-based validation (v1)

        if output is None:
            return {"valid": False, "reason": "empty output"}

        if isinstance(output, str) and len(output) < 5:
            return {"valid": False, "reason": "too short"}

        return {"valid": True, "output": output}