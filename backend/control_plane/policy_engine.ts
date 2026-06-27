export const policyEngine = {
  async check(userId, prompt) {
    let riskScore = 0;

    if (prompt.includes("hack")) riskScore += 80;
    if (prompt.length > 2000) riskScore += 30;

    const allowed = riskScore < 70;

    return {
      allowed,
      riskScore,
      reason: allowed ? "OK" : "HIGH_RISK_CONTENT",
    };
  },
};