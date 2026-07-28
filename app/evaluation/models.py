from dataclasses import dataclass
from typing import List

from app.response import Source


@dataclass
class EvaluationResult:
    question: str
    ground_truth: str
    prediction: str
    contexts: List[str]
    sources: List[Source]
    confidence: float