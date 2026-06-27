class MemoryAgent:

    def __init__(self):
        self.store = []

    def write(self, item):
        self.store.append(item)

    def read(self):
        return self.store[-10:]  # last context