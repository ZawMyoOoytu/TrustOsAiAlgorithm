class SummarizerAgent:

    def run(self, text):

        return {
            "type": "summary",
            "output": f"Summary: {text}"
        }