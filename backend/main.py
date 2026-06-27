from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import logging

# DB
from backend.db.sqlite_db import init_db

# Routers (Control Plane APIs)
from backend.api.run_agent import router as agent_router
from backend.api.executions import router as exec_router
from backend.api.memory import router as memory_router
from backend.websocket.routes import router as ws_router

# Load env
load_dotenv()

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TrustOsAi")


# =========================
# LIFESPAN (SAFE VERSION)
# =========================
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("🚀 starting TrustOsAi backend...")

        init_db()

        logger.info("✅ database ready")

    except Exception as e:
        logger.error(f"❌ startup failed: {e}")
        raise e

    yield

    logger.info("🛑 shutting down TrustOsAi...")


# =========================
# APP INIT
# =========================
app = FastAPI(
    title="TrustOsAi",
    version="1.0.0",
    lifespan=lifespan
)


# =========================
# CORS (DEV SAFE)
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# ROUTERS (CONTROL PLANE)
# =========================

# AI Agent Execution
app.include_router(agent_router, prefix="/api/agent", tags=["Agent"])

# Execution logs / history
app.include_router(exec_router, prefix="/api/executions", tags=["Executions"])

# Memory / context system
app.include_router(memory_router, prefix="/api/memory", tags=["Memory"])

# WebSocket (real-time)
app.include_router(ws_router, prefix="/ws", tags=["WebSocket"])


# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def root():
    return {
        "status": "ok",
        "system": "TrustOsAi",
        "mode": "development"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "backend": "running"
    }