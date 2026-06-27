import time
import uuid

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


async def run_execution(task: str, user_id: str = "anonymous"):

    execution_id = str(uuid.uuid4())
    start = time.time()

    state = {
        "execution_id": execution_id,
        "task": task,
        "user_id": user_id,
        "status": "queued"
    }

    # 1 queued
    save_execution_stage(execution_id, "queued")
    await ws_manager.broadcast(execution_id, {"event": "queued", "data": state})

    # 2 policy
    policy = evaluate_policy(task)
    trust = calculate_trust(policy)

    state.update({
        "policy": policy,
        "trust_score": trust,
        "status": "policy_checked"
    })

    save_execution_stage(execution_id, "policy_checked", extra=policy)
    await ws_manager.broadcast(execution_id, {"event": "policy_checked", "data": state})

    if policy.get("action") == "block":
        state["status"] = "blocked"
        save_execution_stage(execution_id, "blocked")
        save_execution(execution_id, task, state)
        return state

    # 3 billing
    billing_result = billing.charge({"id": user_id, "credits": 1})

    state["billing"] = billing_result
    save_execution_stage(execution_id, "billing", extra=billing_result)

    await ws_manager.broadcast(execution_id, {"event": "billing", "data": state})

    if not billing_result.get("allowed"):
        state["status"] = "blocked"
        save_execution(execution_id, task, state)
        return state

    # 4 running
    state["status"] = "running"
    save_execution_stage(execution_id, "running")
    await ws_manager.broadcast(execution_id, {"event": "running", "data": state})

    # 5 planning
    prompt = build_reasoning_context(task, policy, trust)
    save_execution_stage(execution_id, "planning")

    # 6 llm
    raw = llm_plan(prompt)
    save_execution_stage(execution_id, "llm_call")

    parsed = safe_parse_llm_output(raw)

    # 7 memory
    store_memory(user_id, task, parsed)
    save_execution_stage(execution_id, "memory_write")

    # 8 final
    runtime = int((time.time() - start) * 1000)

    state.update({
        "status": "completed",
        "runtime_ms": runtime,
        "result": parsed,
        "trust_score": trust
    })

    save_execution_stage(execution_id, "completed")
    await ws_manager.broadcast(execution_id, {"event": "completed", "data": state})

    save_execution(execution_id, task, state)

    return state