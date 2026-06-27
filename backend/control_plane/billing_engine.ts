const userCredits = new Map<string, number>([
  ["user1", 10],
]);

const COST_TABLE = {
  chat: 1,
  essay: 3,
  agent: 5,
};

export const billingEngine = {
  async check(userId, taskType) {
    const credits = userCredits.get(userId) || 0;
    const cost = COST_TABLE[taskType] || 1;

    return {
      allowed: credits >= cost,
      cost,
    };
  },

  async deduct(userId, cost) {
    const current = userCredits.get(userId) || 0;
    userCredits.set(userId, current - cost);
  },
};