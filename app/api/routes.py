from fastapi import APIRouter, HTTPException

from app.api.metrics import MetricsService

from app.ingestion.manager import KnowledgeBaseManager
from app.api.schemas import IngestionRequest
from app.api.schemas import (
    ChatRequest,
    ChatResponse,
    SourceResponse,
)
from app.rag.rag_engine import RAGEngine


router = APIRouter()

rag = RAGEngine()
metrics = MetricsService()
ingestion = KnowledgeBaseManager()

@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):

    try:

        response = rag.answer(request.question)

        return ChatResponse(
            answer=response.answer,
            confidence=response.confidence,
            sources=[
                SourceResponse(
                    title=source.title,
                    url=source.url,
                )
                for source in response.sources
            ],
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "AI Documentation Assistant",
        "version": "1.0.0",
    }


@router.get("/metrics")
def metrics_endpoint():

    return metrics.get_metrics()


@router.post("/ingest")
def ingest(request: IngestionRequest):

    try:

        ingestion.ingest(request.url)

        return {
            "status": "success",
            "message": "Knowledge base indexed successfully."
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )