class WorkerNode:

    def __init__(self, executor, validator, memory):

        self.executor = executor
        self.validator = validator
        self.memory = memory

    def process(self, task):

        raw = self.executor.run(task)
        validated = self.validator.run(raw)

        self.memory.write({
            "task": task,
            "result": validated
        })

        return validated