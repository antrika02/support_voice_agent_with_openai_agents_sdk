from fastapi import (
    APIRouter,
    Depends,
    status,
)

from app.api.dependencies import (
    get_rag_engine,
    get_metrics_service,
    get_ingestion_manager,
)

from app.api.metrics import MetricsService
from app.api.schemas import (
    ChatRequest,
    ChatResponse,
    SourceResponse,
    IngestionRequest,
)

from app.ingestion.manager import KnowledgeBaseManager
from app.logging import get_logger
from app.rag.rag_engine import RAGEngine


logger = get_logger(__name__)

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse,
    summary="Ask a documentation question",
    description=(
        "Runs the Retrieval-Augmented Generation (RAG) pipeline "
        "to answer questions using the indexed documentation."
    ),
)
def chat(
    request: ChatRequest,
    rag: RAGEngine = Depends(get_rag_engine),
) -> ChatResponse:
    """
    Answer a documentation question using the RAG pipeline.
    """

    logger.info("Received chat request.")

    response = rag.answer(request.question)

    logger.info(
        "Successfully generated response "
        f"(confidence={response.confidence:.2f})"
    )

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


@router.get(
    "/health",
    summary="Health check",
    description="Returns the health status of the application.",
)
def health():
    """
    Health check endpoint.
    """

    logger.info("Health endpoint called.")

    return {
        "status": "healthy",
        "service": "AI Documentation Assistant",
        "version": "1.0.0",
    }


@router.get(
    "/metrics",
    summary="Application metrics",
    description="Returns runtime metrics for the RAG service.",
)
def metrics_endpoint(
    metrics: MetricsService = Depends(
        get_metrics_service,
    ),
):
    """
    Return application metrics.
    """

    logger.info("Metrics endpoint called.")

    return metrics.get_metrics()


@router.post(
    "/ingest",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Ingest documentation",
    description=(
        "Discovers, crawls, chunks, embeds and indexes "
        "documentation into the vector database."
    ),
)
def ingest(
    request: IngestionRequest,
    ingestion: KnowledgeBaseManager = Depends(
        get_ingestion_manager,
    ),
):
    """
    Trigger documentation ingestion.
    """

    logger.info(
        f"Received ingestion request for: {request.url}"
    )

    ingestion.ingest(request.url)

    logger.info(
        "Knowledge base indexed successfully."
    )

    return {
        "status": "success",
        "message": "Knowledge base indexed successfully.",
    }