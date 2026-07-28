from typing import Any


class ConfidenceCalculator:
    """
    Calculates a confidence score based on retrieval similarity scores.

    The heuristic combines:
    - Top retrieval score (70%)
    - Average retrieval score (30%)

    This rewards highly relevant matches while also considering the
    overall quality of the retrieved context.
    """

    TOP_SCORE_WEIGHT = 0.7
    AVERAGE_SCORE_WEIGHT = 0.3

    @classmethod
    def calculate(
        cls,
        results: list[Any],
    ) -> float:
        """
        Calculate a confidence score for retrieved documents.

        Args:
            results: Retrieved search results.

        Returns:
            Confidence score between 0.0 and 1.0.
        """

        if not results:
            return 0.0

        scores = [
            result.score
            for result in results
        ]

        top_score = max(scores)

        average_score = (
            sum(scores) / len(scores)
        )

        confidence = (
            cls.TOP_SCORE_WEIGHT * top_score
            + cls.AVERAGE_SCORE_WEIGHT * average_score
        )

        # Clamp confidence to [0.0, 1.0]
        return max(
            0.0,
            min(confidence, 1.0),
        )