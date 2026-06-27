from backend.engine.structured_guard import StructuredModeGuard
from backend.engine.output_enforcer import OutputEnforcer
import json

guard = StructuredModeGuard()
enforcer = OutputEnforcer()


def structured_llm(task: str, llm_call_func, mode: str, schema: dict):

    # 1. BUILD STRICT PROMPT
    prompt = guard.build_structured_prompt(
        task=task,
        schema=schema,
        mode=mode
    )

    # 2. CALL LLM
    raw_output = llm_call_func(prompt)

    # 3. HARD ENFORCEMENT (IMPORTANT)
    result = enforcer.enforce(raw_output, mode)

    return result