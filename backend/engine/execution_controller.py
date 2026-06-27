from engine.contract_enforcer import enforce_policy
from engine.billing import check_and_deduct
from engine.execution_engine import run_llm
from engine.analytics import log_execution

class ExecutionController:

    def execute(self, request):

        user_id = request["user_id"]
        prompt = request["prompt"]
        task_type = request["task_type"]

        # 1. POLICY GATE (HARD STOP)
        policy = enforce_policy(user_id, prompt)

        if not policy["allowed"]:
            return {
                "status": "blocked",
                "stage": "policy",
                "reason": policy["reason"]
            }

        # 2. BILLING GATE (HARD STOP)
        billing = check_and_deduct(user_id, task_type)

        if not billing["allowed"]:
            return {
                "status": "blocked",
                "stage": "billing",
                "reason": "INSUFFICIENT_CREDITS"
            }

        # 3. EXECUTION
        result = run_llm(task_type, prompt)

        # 4. LOGGING
        log_execution({
            "user_id": user_id,
            "prompt": prompt,
            "task_type": task_type,
            "result": result
        })

        return {
            "status": "success",
            "output": result
        }