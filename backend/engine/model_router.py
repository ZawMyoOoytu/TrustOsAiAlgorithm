import os
import time
import logging
from typing import Dict, Any

from backend.llm.planner import llm_plan  # default model (Groq/OpenAI wrapper)


# =========================
# MODEL ROUTING STRATEGY
# =========================
def choose_model(task: str, trust_score: float) -> str:

    task_lower = task.lower()

    # cheap fast tasks
    if len(task_lower) < 30:
        return "fast"

    # complex reasoning
    if "essay" in task_lower or "analysis" in task_lower:
        return "smart"

    # high trust required
    if trust_score < 0.5:
        return "safe"

    return "balanced"


# =========================
# MODEL EXECUTION (MOCK MULTI PROVIDER)
# =========================
def run_model(model: str, prompt: str) -> str:

    start = time.time()

    try:

        # 🔥 HERE you can plug real providers later

        if model == "fast":
            result = llm_plan(prompt)  # cheap/fast model

        elif model == "smart":
            result = llm_plan(prompt)  # future: GPT-4 / Claude

        elif model == "safe":
            result = llm_plan(prompt)  # stricter model

        else:
            result = llm_plan(prompt)

        latency = int((time.time() - start) * 1000)

        logging.info(f"[MODEL] {model} used | {latency}ms")

        return result

    except Exception as e:
        logging.error(f"[MODEL ERROR] {e}")

        # fallback model
        return llm_plan(prompt)