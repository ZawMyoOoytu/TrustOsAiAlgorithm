import time

EXECUTION_DB = {}

def start_execution(execution_id, task):
    EXECUTION_DB[execution_id] = {
        "task": task,
        "status": "running",
        "start_time": time.time(),
        "steps": []
    }

def finish_execution(execution_id, result):
    EXECUTION_DB[execution_id]["status"] = "completed"
    EXECUTION_DB[execution_id]["result"] = result
    EXECUTION_DB[execution_id]["end_time"] = time.time()

def get_execution(execution_id):
    return EXECUTION_DB.get(execution_id)