const WS_BASE = "ws://127.0.0.1:8000";

class ExecutionSocket {
  constructor() {
    this.socket = null;
    this.listeners = {};
  }

  connect(executionId) {
    this.socket = new WebSocket(
      `${WS_BASE}/ws/execution/${executionId}`
    );

    this.socket.onopen = () => {
      console.log("🟢 WebSocket connected:", executionId);
    };

    this.socket.onmessage = (event) => {
      const data = JSON.parse(event.data);

      const handler = this.listeners[data.event];
      if (handler) {
        handler(data);
      }
    };

    this.socket.onclose = () => {
      console.log("🔴 WebSocket disconnected");
    };
  }

  on(event, callback) {
    this.listeners[event] = callback;
  }

  send(data) {
    if (this.socket && this.socket.readyState === 1) {
      this.socket.send(JSON.stringify(data));
    }
  }

  disconnect() {
    if (this.socket) {
      this.socket.close();
    }
  }
}

export default new ExecutionSocket();