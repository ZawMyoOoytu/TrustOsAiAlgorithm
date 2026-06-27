import time
import uuid
import logging
from typing import Dict, Any

from backend.engine.policy_engine import evaluate_policy
from backend.engine.trust_engine import calculate_trust
from backend.engine.reasoning_engine import build_reasoning_context
from backend.llm.planner import llm_plan
from backend.core.llm_parser import safe_parse_llm_output
from backend.engine.billing import BillingEngine
from backend.memory.memory import store_memory

from backend.db.sqlite_db import save_execution, save_execution_stage
from backend.websocket.manager import ws_manager


billing = BillingEngine()


# =========================
# SAFE WS EMIT (NO CRASH)
# =========================
async def emit(execution_id: str, event: str, state: dict, extra: dict = None):
    payload = {
        "execution_id": execution_id,
        "event": event,
        "stage": event,
        "status": state.get("status"),
        "data": state,
        "extra": extra or {},
        "timestamp": time.time()
    }

    try:
        await ws_manager.broadcast(execution_id, payload)
    except Exception as e:
        logging.warning(f"WS error ignored: {e}")


# =========================
# MAIN ENGINE (SAFE VERSION)
# =========================
async def run_execution(task: str, user_id: str = "anonymous"):

    execution_id = str(uuid.uuid4())
    start = time.time()

    state = {
        "execution_id": execution_id,
        "task": task,
        "user_id": user_id,
        "status": "queued",
        "trust_score": 0,
        "policy": {},
        "billing": {},
        "result": {},
        "runtime_ms": 0
    }

    try:

        # ================= QUEUED =================
        await emit(execution_id, "queued", state)

        # ================= POLICY =================
        policy = evaluate_policy(task)
        trust = calculate_trust(policy)

        state["policy"] = policy
        state["trust_score"] = trust

        await emit(execution_id, "policy_checked", state, policy)

        if policy.get("action") == "block":
            state["status"] = "blocked"

            save_execution(execution_id, task, state)
            await emit(execution_id, "blocked", state)

            return {"status": "blocked", "data": state}

        # ================= BILLING =================
        billing_result = billing.check(user_id, "agent")  # FIXED (no charge())

        state["billing"] = billing_result
        await emit(execution_id, "billing", state, billing_result)

        if not billing_result.get("allowed", False):
            state["status"] = "blocked"

            save_execution(execution_id, task, state)
            await emit(execution_id, "blocked", state)

            return {"status": "blocked", "data": state}

        billing.deduct(user_id, "agent")

        # ================= RUNNING =================
        state["status"] = "running"
        await emit(execution_id, "running", state)

        # ================= PLANNING =================
        prompt = build_reasoning_context(task, policy, trust)
        await emit(execution_id, "planning", state)

        # ================= LLM CALL =================
        raw = llm_plan(prompt)
        await emit(execution_id, "llm_call", state)

        parsed = safe_parse_llm_output(raw)

        # ================= MEMORY =================
        store_memory(user_id, task, parsed)
        await emit(execution_id, "memory_write", state)

        # ================= FINAL =================
        state["status"] = "completed"
        state["runtime_ms"] = int((time.time() - start) * 1000)
        state["result"] = parsed

        save_execution(execution_id, task, state)
        await emit(execution_id, "completed", state)

        return {
            "status": "success",
            "data": state
        }

    except Exception as e:
        logging.error(f"Execution crash: {e}")

        state["status"] = "error"
        state["error"] = str(e)

        save_execution(execution_id, task, state)
        await emit(execution_id, "error", state)

        return {
            "status": "error",
            "message": str(e),
            "data": state
        }