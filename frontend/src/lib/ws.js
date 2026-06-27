export function createExecutionSocket(executionId, onMessage) {
  const ws = new WebSocket(`ws://localhost:8000/ws/execution/${executionId}`);

  ws.onopen = () => {
    console.log("WS connected:", executionId);
  };

  ws.onmessage = (event) => {
    try {
      const msg = JSON.parse(event.data);
      onMessage(msg);
    } catch (e) {
      console.error("WS parse error", e);
    }
  };

  ws.onerror = (err) => console.error("WS error", err);

  return ws;
}