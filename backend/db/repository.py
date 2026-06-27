from typing import Dict, List, Optional
import threading
import json
import os

_db_lock = threading.Lock()

EXECUTIONS_DB: Dict[str, dict] = {}

PERSIST_FILE = "executions_db.json"


# =========================
# LOAD FROM DISK (startup)
# =========================
def load_db():
    global EXECUTIONS_DB
    if os.path.exists(PERSIST_FILE):
        try:
            with open(PERSIST_FILE, "r", encoding="utf-8") as f:
                EXECUTIONS_DB = json.load(f)
                print(f"✅ DB LOADED: {len(EXECUTIONS_DB)} records")
        except Exception as e:
            print("❌ DB LOAD ERROR:", e)


# =========================
# SAVE TO DISK
# =========================
def _persist():
    try:
        with open(PERSIST_FILE, "w", encoding="utf-8") as f:
            json.dump(EXECUTIONS_DB, f, indent=2)
    except Exception as e:
        print("❌ DB SAVE ERROR:", e)


# =========================
# SAVE EXECUTION
# =========================
def save_execution(execution_id: str, task: str, response: dict):
    with _db_lock:
        EXECUTIONS_DB[execution_id] = {
            "execution_id": execution_id,
            "task": task,
            "status": response.get("status", "completed"),
            "trust_score": response.get("trust_score", 0),
            "runtime_ms": response.get("runtime_ms", 0),
            "result": response.get("result", {}),
        }

        print("💾 SAVED EXECUTION:", execution_id)

        _persist()


# =========================
# GET SINGLE
# =========================
def get_execution(execution_id: str):
    return EXECUTIONS_DB.get(execution_id)


# =========================
# LIST ALL
# =========================
def list_executions() -> List[dict]:
    return list(EXECUTIONS_DB.values())


def get_all_executions():
    return list_executions()