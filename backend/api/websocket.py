from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from backend.websocket.manager import ws_manager

router = APIRouter()


# =========================
# EXECUTION WEBSOCKET ROUTE
# =========================
@router.websocket("/ws/execution/{execution_id}")
async def execution_ws(websocket: WebSocket, execution_id: str):

    # connect client to execution room
    await ws_manager.connect(execution_id, websocket)

    try:
        while True:
            # keep connection alive (frontend may send ping or ignore)
            await websocket.receive_text()

    except WebSocketDisconnect:
        ws_manager.disconnect(execution_id, websocket)

    except Exception:
        # safety fallback (prevents server crash)
        ws_manager.disconnect(execution_id, websocket)