import { useEffect, useState } from "react";

export default function ExecutionTimeline({ executionId }) {
  const [timeline, setTimeline] = useState([]);

  useEffect(() => {
    if (!executionId) return;

    const ws = new WebSocket(
      `ws://127.0.0.1:8000/ws/execution/${executionId}`
    );

    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);

      console.log("LIVE EVENT:", msg);

      setTimeline((prev) => [
        ...prev,
        {
          stage: msg.event,
          status: "running",
          time: Date.now(),
          extra: msg.extra || {},
        },
      ]);
    };

    return () => ws.close();
  }, [executionId]);

  return (
    <div>
      <h3>Execution Timeline</h3>

      {timeline.length === 0 && <p>No live events yet...</p>}

      {timeline.map((t, i) => (
        <div key={i}>
          <b>{t.stage}</b> — {t.status}
        </div>
      ))}
    </div>
  );
}