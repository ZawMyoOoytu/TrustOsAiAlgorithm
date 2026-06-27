from fastapi import APIRouter, WebSocket
from backend.websocket.manager import ws_manager

router = APIRouter()


@router.websocket("/ws/execution/{execution_id}")
async def execution_ws(websocket: WebSocket, execution_id: str):

    await ws_manager.connect(execution_id, websocket)

    try:
        while True:
            # keep alive (client can send ping)
            await websocket.receive_text()

    except Exception:
        ws_manager.disconnect(execution_id, websocket)