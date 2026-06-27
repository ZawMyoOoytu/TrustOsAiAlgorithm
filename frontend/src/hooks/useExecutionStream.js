import { useEffect, useState } from "react";

export default function useExecutionStream(executionId) {
  const [logs, setLogs] = useState([]);
  const [status, setStatus] = useState("connecting");
  const [trustScore, setTrustScore] = useState(0);

  useEffect(() => {
    if (!executionId) return;

    const ws = new WebSocket(
      `ws://127.0.0.1:8000/ws/execution/${executionId}`
    );

    ws.onopen = () => setStatus("running");

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);

      if (data.type === "session") {
        setTrustScore(data.trust_score || 50);
        return;
      }

      if (data.type === "result") {
        setStatus("completed");
      }

      setLogs((prev) => [
        ...prev,
        {
          type: data.type,
          message: data.message,
          latency: data.latency, // ⭐ IMPORTANT
        },
      ]);

      if (typeof data.trust_score === "number") {
        setTrustScore(data.trust_score);
      }
    };

    ws.onerror = () => setStatus("failed");
    ws.onclose = () => setStatus("completed");

    return () => ws.close();
  }, [executionId]);

  return { logs, status, trustScore };
}