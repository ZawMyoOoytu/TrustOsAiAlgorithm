import sqlite3
import json
import threading
from pathlib import Path
from typing import Optional, List, Dict, Any

# =========================
# DB PATH
# =========================
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "trustos.db"

_db_lock = threading.Lock()


# =========================
# CONNECTION
# =========================
def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# SAFE JSON
# =========================
def safe_json_load(data: Any) -> Dict:
    try:
        if not data:
            return {}
        return json.loads(data)
    except Exception:
        return {}


# =========================
# INIT DB
# =========================
def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS executions (
            execution_id TEXT PRIMARY KEY,
            task TEXT,
            status TEXT DEFAULT 'pending',
            trust_score REAL DEFAULT 0,
            runtime_ms INTEGER DEFAULT 0,
            result TEXT DEFAULT '{}'
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS execution_stages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            execution_id TEXT,
            stage TEXT,
            status TEXT,
            timestamp REAL,
            extra TEXT
        )
    """)

    conn.commit()
    conn.close()


# =========================
# SAVE EXECUTION
# =========================
def save_execution(execution_id: str, task: str, state: dict):

    with _db_lock:
        conn = get_connection()

        conn.execute("""
            INSERT OR REPLACE INTO executions (
                execution_id, task, status, trust_score, runtime_ms, result
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            execution_id,
            task,
            state.get("status", "completed"),
            float(state.get("trust_score", 0) or 0),
            int(state.get("runtime_ms", 0) or 0),
            json.dumps(state.get("result", {}))
        ))

        conn.commit()
        conn.close()


# =========================
# SAVE STAGE
# =========================
def save_execution_stage(
    execution_id: str,
    stage: str,
    status: str = "done",
    extra: dict = None
):

    with _db_lock:
        conn = get_connection()

        conn.execute("""
            INSERT INTO execution_stages (
                execution_id,
                stage,
                status,
                timestamp,
                extra
            ) VALUES (?, ?, ?, ?, ?)
        """, (
            execution_id,
            stage,
            status,
            __import__("time").time(),
            json.dumps(extra or {})
        ))

        conn.commit()
        conn.close()


# =========================
# GET EXECUTION (FIXED)
# =========================
def get_execution(execution_id: str) -> Optional[dict]:

    conn = get_connection()

    row = conn.execute(
        "SELECT * FROM executions WHERE execution_id=?",
        (execution_id,)
    ).fetchone()

    if not row:
        return None

    stages = conn.execute(
        "SELECT * FROM execution_stages WHERE execution_id=? ORDER BY id ASC",
        (execution_id,)
    ).fetchall()

    conn.close()

    return {
        "execution_id": row["execution_id"],
        "task": row["task"],
        "status": row["status"],
        "trust_score": row["trust_score"],
        "runtime_ms": row["runtime_ms"],
        "result": safe_json_load(row["result"]),
        "stages": [
            {
                "stage": s["stage"],
                "status": s["status"],
                "timestamp": s["timestamp"],
                "extra": safe_json_load(s["extra"])
            }
            for s in stages
        ]
    }


# =========================
# GET ALL
# =========================
def get_all_executions() -> List[dict]:

    conn = get_connection()

    rows = conn.execute("""
        SELECT * FROM executions ORDER BY rowid DESC
    """).fetchall()

    conn.close()

    return [
        {
            "execution_id": r["execution_id"],
            "task": r["task"],
            "status": r["status"],
            "trust_score": r["trust_score"],
            "runtime_ms": r["runtime_ms"],
        }
        for r in rows
    ]