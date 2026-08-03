from pydantic import BaseModel
from typing import List


class ChatRequest(BaseModel):
    """
    Incoming chat request.
    """

    question: str


class SourceResponse(BaseModel):
    """
    Source document returned with an answer.
    """

    title: str
    url: str


class ChatResponse(BaseModel):
    """
    Response returned by the RAG API.
    """

    answer: str

    confidence: float

    sources: List[SourceResponse]


class IngestionRequest(BaseModel):
    """
    Trigger indexing of a documentation website.
    """

    url: str