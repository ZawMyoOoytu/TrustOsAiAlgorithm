import { policyEngine } from "../control_plane/policy_engine";
import { billingEngine } from "../control_plane/billing_engine";
import { orchestrator } from "../control_plane/orchestrator";
import { executeLLM } from "../execution_plane/llm_executor";
import { logger } from "../observability/logger";

export async function handleRequest(req) {
  const { userId, prompt, taskType } = req;

  logger.info("Request received", { userId, taskType });

  // 1. POLICY CHECK (PRE EXECUTION)
  const policy = await policyEngine.check(userId, prompt);

  if (!policy.allowed) {
    logger.warn("Blocked by policy", policy);
    return { error: "BLOCKED_BY_POLICY", reason: policy.reason };
  }

  // 2. BILLING CHECK (PRE EXECUTION)
  const billing = await billingEngine.check(userId, taskType);

  if (!billing.allowed) {
    logger.warn("Blocked by billing", billing);
    return { error: "INSUFFICIENT_CREDITS" };
  }

  // 3. ORCHESTRATION (MODEL SELECTION)
  const model = await orchestrator.select(taskType, prompt);

  logger.info("Model selected", { model });

  // 4. EXECUTION
  const result = await executeLLM(model, prompt);

  // 5. POST PROCESS
  await billingEngine.deduct(userId, billing.cost);

  logger.info("Execution completed", {
    userId,
    cost: billing.cost,
    model,
  });

  return {
    output: result,
    model,
    cost: billing.cost,
    trust: policy.riskScore,
  };
}