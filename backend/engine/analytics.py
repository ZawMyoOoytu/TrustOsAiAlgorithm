from backend.db.sqlite_db import get_all_executions

def get_dashboard_stats():

    executions = get_all_executions()

    total = len(executions)

    if total == 0:
        return {
            "total_executions": 0,
            "success_rate": 0,
            "avg_latency": 0
        }

    success = 0
    total_runtime = 0

    for e in executions:
        if e.get("status") == "completed":
            success += 1

        total_runtime += e.get("runtime_ms", 0)

    return {
        "total_executions": total,
        "success_rate": round(success / total * 100, 2),
        "avg_latency": int(total_runtime / total)
    }