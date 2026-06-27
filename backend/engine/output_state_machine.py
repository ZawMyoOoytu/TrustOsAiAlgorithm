import json

class OutputStateMachine:

    def __init__(self):
        pass

    def enforce(self, mode: str, raw_output: str):

        # 🔥 STRUCTURED MODE = ONLY VALID JSON ALLOWED
        if mode.startswith("structured"):

            # STEP 1: MUST BE JSON
            try:
                data = json.loads(raw_output)
            except Exception:
                return {
                    "state": "REJECTED",
                    "reason": "Output is not valid JSON",
                    "raw": raw_output
                }

            # STEP 2: MUST NOT CONTAIN TEXT BEHAVIOR
            forbidden_patterns = [
                "step",
                "first",
                "then",
                "you should",
                "we will",
                "to do this",
                "html",
                "css",
                "javascript"
            ]

            raw_lower = raw_output.lower()

            for p in forbidden_patterns:
                if p in raw_lower:
                    return {
                        "state": "REJECTED",
                        "reason": f"Forbidden pattern detected: {p}",
                        "raw": raw_output
                    }

            # STEP 3: ACCEPTED STRUCTURED OUTPUT
            return {
                "state": "ACCEPTED",
                "data": data
            }

        # NORMAL MODE
        return {
            "state": "FREE",
            "data": raw_output
        }