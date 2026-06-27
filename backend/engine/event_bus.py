import time
from backend.websocket.manager import ws_manager

class EventBus:

    async def publish(self, execution_id: str, event: str, state: dict = None, extra: dict = None):

        payload = {
            "execution_id": execution_id,
            "event": event,
            "data": state or {},
            "extra": extra or {},
            "timestamp": time.time()
        }

        # 🔥 SINGLE SOURCE OF TRUTH FOR UI
        await ws_manager.broadcast(execution_id, payload)


event_bus = EventBus()