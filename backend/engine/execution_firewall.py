import json

class ExecutionFirewall:

    def build_strict_packet(self, task: str, contract: dict, mode: str):

        if mode.startswith("structured"):

            # 🔥 HARD ROLE LOCK (IMPORTANT ADDITION)
            return json.dumps({
                "SYSTEM": "EXECUTION_ONLY_MODE",

                "ROLE": {
                    "LLM_BEHAVIOR": "PURE_TRANSFORMER",
                    "FORBIDDEN": [
                        "explain",
                        "describe",
                        "teach",
                        "elaborate",
                        "reason",
                        "steps",
                        "guide"
                    ],
                    "ALLOWED": [
                        "return_json_only",
                        "map_input_to_schema"
                    ]
                },

                "CONTRACT": contract,

                "TASK": task,

                "OUTPUT_RULE": "STRICT_JSON_ONLY_NO_TEXT"
            })

        return task