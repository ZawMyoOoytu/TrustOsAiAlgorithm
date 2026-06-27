from collections import deque


class ExecutionQueue:

    def __init__(self):
        self.queue = deque()

    def push(self, task):
        self.queue.append(task)

    def pop(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def empty(self):
        return len(self.queue) == 0