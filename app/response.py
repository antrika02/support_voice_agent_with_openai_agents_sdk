from dataclasses import dataclass
from typing import List


@dataclass
class Source:
    """
    Represents one source used to answer a question.
    """
    title: str
    url: str


@dataclass

class RAGResponse:

    answer: str

    sources: List[Source]

    confidence: float

    contexts: List[str] 