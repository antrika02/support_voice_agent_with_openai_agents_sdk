from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class SourceResponse(BaseModel):
    title: str
    url: str


class ChatResponse(BaseModel):
    answer: str
    confidence: float | None
    sources: list[SourceResponse]