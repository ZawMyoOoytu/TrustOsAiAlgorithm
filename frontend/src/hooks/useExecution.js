import { useEffect } from "react";
import { useExecutionStore } from "../store/executionStore";
import { createExecutionSocket } from "../lib/ws";

export function useExecution(executionId) {
  const upsertExecution = useExecutionStore((s) => s.upsertExecution);

  useEffect(() => {
    if (!executionId) return;

    const ws = createExecutionSocket(executionId, (msg) => {
      const { data } = msg;

      if (!data) return;

      // 🔥 NORMALIZE EVERY WS UPDATE
      upsertExecution({
        ...data,
        execution_id: data.execution_id,
      });
    });

    return () => ws.close();
  }, [executionId]);

  return useExecutionStore((s) => s.executions[executionId]);
}