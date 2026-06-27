import { create } from "zustand";

export const useExecutionStore = create((set, get) => ({
  executions: {},

  upsertExecution: (execution) => {
    set((state) => ({
      executions: {
        ...state.executions,
        [execution.execution_id]: {
          ...(state.executions[execution.execution_id] || {}),
          ...execution,
        },
      },
    }));
  },

  updateExecution: (id, patch) => {
    set((state) => ({
      executions: {
        ...state.executions,
        [id]: {
          ...(state.executions[id] || {}),
          ...patch,
        },
      },
    }));
  },
}));