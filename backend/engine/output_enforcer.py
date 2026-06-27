import json

class OutputEnforcer:

    def validate(self, raw_output: str, mode: str):

        if mode.startswith("structured"):

            try:
                data = json.loads(raw_output)

                # HARD CHECK: must be dict
                if not isinstance(data, dict):
                    raise ValueError()

                return data

            except Exception:

                # 🚨 FORCE FAILURE STATE
                return {
                    "status": "rejected",
                    "reason": "non-structured output detected",
                    "raw_output": raw_output
                }

        return {
            "status": "free_mode",
            "output": raw_output
        }