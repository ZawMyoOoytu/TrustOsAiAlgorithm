class ToolRegistry:

    def __init__(self):
        self.tools = {
            "draw_website": self.draw_website,
            "save_data": self.save_data,
            "fetch_data": self.fetch_data
        }

    def get(self, name):
        return self.tools.get(name)

    # -------------------------
    # SAMPLE TOOLS
    # -------------------------

    def draw_website(self, input_data):
        return {
            "type": "website_layout",
            "data": {
                "header": True,
                "hero": True,
                "content": True,
                "footer": True
            }
        }

    def save_data(self, input_data):
        return {"status": "saved", "input": input_data}

    def fetch_data(self, input_data):
        return {"status": "fetched", "data": {}}