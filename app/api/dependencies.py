from fastapi import Request

from app.rag.rag_engine import RAGEngine
from app.api.metrics import MetricsService
from app.ingestion.manager import KnowledgeBaseManager


def get_rag_engine(request: Request) -> RAGEngine:
    """
    Return the shared RAG engine.
    """
    return request.app.state.rag_engine


def get_metrics_service(
    request: Request,
) -> MetricsService:
    """
    Return the shared metrics service.
    """
    return request.app.state.metrics_service


def get_ingestion_manager(
    request: Request,
) -> KnowledgeBaseManager:
    """
    Return the shared ingestion manager.
    """
    return request.app.state.ingestion_manager