class ExecutionLock:

    def enforce_mode(self, mode: str, raw_output: str):

        if mode.startswith("structured"):

            # 🚨 BLOCK ANY NON-STRUCTURED OUTPUT
            forbidden_signals = [
                "```html",
                "```css",
                "```javascript",
                "Step",
                "First",
                "Then",
                "Finally",
                "We will",
                "You should"
            ]

            for word in forbidden_signals:
                if word.lower() in raw_output.lower():
                    return {
                        "status": "violated",
                        "reason": "LLM produced explanatory/tutorial content in structured mode",
                        "raw_output": raw_output
                    }

        return {
            "status": "ok",
            "output": raw_output
        }