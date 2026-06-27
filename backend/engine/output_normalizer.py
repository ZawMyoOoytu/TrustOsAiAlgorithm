import json
import re

class OutputNormalizer:

    def normalize(self, raw_output: str):

        # =========================
        # STEP 1: TRY PARSE JSON
        # =========================
        try:
            return json.loads(raw_output)
        except:
            pass

        # =========================
        # STEP 2: EXTRACT JSON BLOCK
        # =========================
        match = re.search(r"\{.*\}", raw_output, re.DOTALL)

        if match:
            try:
                return json.loads(match.group(0))
            except:
                pass

        # =========================
        # STEP 3: FORCE STRUCTURE FALLBACK
        # =========================
        return {
            "type": "unstructured_output",
            "data": {
                "raw": raw_output
            }
        }