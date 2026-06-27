MEMORY_DB = []


def store_memory(user_id: str, task: str, result: str):
    MEMORY_DB.append({
        "user_id": user_id,
        "task": task,
        "result": result
    })


def get_memory(user_id: str):
    return [
        m for m in MEMORY_DB
        if m["user_id"] == user_id
    ]