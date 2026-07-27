from dataclasses import dataclass


@dataclass
class Source:
    """
    Represents one source used to answer a question.
    """
    title: str
    url: str


@dataclass
class RAGResponse:
    """
    Represents the final response returned by the RAG engine.
    """
    answer: str
    sources: list[Source]
    confidence: float | None = None