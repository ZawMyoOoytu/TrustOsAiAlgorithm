export const orchestrator = {
  async select(taskType, prompt) {
    if (taskType === "chat") return "gpt-small";
    if (taskType === "essay") return "gpt-4-class";
    if (taskType === "agent") return "gpt-agent-model";

    if (prompt.length > 2000) return "gpt-strong";

    return "default-model";
  },
};