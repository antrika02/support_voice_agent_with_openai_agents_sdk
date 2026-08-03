from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import ALLOWED_ORIGINS

from app.api.metrics import MetricsService
from app.api.routes import router
from app.ingestion.manager import KnowledgeBaseManager
from app.logging import get_logger
from app.middleware.exception_handler import (
    register_exception_handlers,
)
from app.middleware.request_logging import (
    register_request_logging,
)
from app.middleware.timing import (
    register_timing_middleware,
)
from app.rag.rag_engine import RAGEngine

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Initialize shared application services on startup
    and clean up resources on shutdown.
    """

    logger.info("Starting AI Documentation Assistant...")

    app.state.rag_engine = RAGEngine()
    app.state.metrics_service = MetricsService()
    app.state.ingestion_manager = KnowledgeBaseManager()

    logger.info("Application startup completed.")

    yield

    logger.info("Shutting down application...")


app = FastAPI(
    title="AI Documentation Assistant",
    version="1.0.0",
    description="Conversational RAG API powered by Gemini and Qdrant.",
    lifespan=lifespan,
)

# ----------------------------------------------------
# CORS
# ----------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------------------
# Custom Middleware
# ----------------------------------------------------

register_request_logging(app)
register_timing_middleware(app)

# ----------------------------------------------------
# Exception Handlers
# ----------------------------------------------------

register_exception_handlers(app)

# ----------------------------------------------------
# API Routes
# ----------------------------------------------------

app.include_router(router)