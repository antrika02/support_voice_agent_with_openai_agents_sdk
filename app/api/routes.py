from fastapi import APIRouter

from app.rag_engine import RAGEngine
from app.api.schemas import (
    ChatRequest,
    ChatResponse,
    SourceResponse,
)

router = APIRouter()

rag = RAGEngine()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):
    """
    Chat with the AI assistant.
    """

    response = rag.answer(request.question)

    return ChatResponse(
        answer=response.answer,
        confidence=response.confidence,
        sources=[
            SourceResponse(
                title=source.title,
                url=source.url
            )
            for source in response.sources
        ]
    )