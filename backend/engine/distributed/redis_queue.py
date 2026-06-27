import redis
import json


class RedisQueue:

    def __init__(self, host="localhost", port=6379):
        self.r = redis.Redis(host=host, port=port, decode_responses=True)

    def push(self, queue_name, task: dict):
        self.r.lpush(queue_name, json.dumps(task))

    def pop(self, queue_name):
        data = self.r.rpop(queue_name)
        if data:
            return json.loads(data)
        return None

    def size(self, queue_name):
        return self.r.llen(queue_name)