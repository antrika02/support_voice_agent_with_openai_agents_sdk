class ConfidenceCalculator:
    """
    Calculates confidence based on retrieval scores.
    """

    @staticmethod
    def calculate(results) -> float:
        if not results:
            return 0.0

        scores = [result.score for result in results]

        top_score = max(scores)
        average_score = sum(scores) / len(scores)

        confidence = (
            0.7 * top_score +
            0.3 * average_score
        )

        return confidence