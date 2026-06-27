import json
from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.active = {}

    async def connect(self, execution_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active.setdefault(execution_id, []).append(websocket)

    def disconnect(self, execution_id: str, websocket: WebSocket):
        self.active[execution_id].remove(websocket)

    async def broadcast(self, execution_id: str, message: dict):
        if execution_id not in self.active:
            return

        data = json.dumps(message)

        for ws in self.active[execution_id]:
            await ws.send_text(data)

ws_manager = ConnectionManager()