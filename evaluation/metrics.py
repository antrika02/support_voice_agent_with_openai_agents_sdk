import json


class EvaluationMetrics:

    def __init__(self, path="evaluation/results.json"):

        with open(path, "r") as f:
            self.results = json.load(f)

    def average_confidence(self):

        return sum(
            r["confidence"]
            for r in self.results
        ) / len(self.results)

    def average_answer_length(self):

        return sum(
            len(r["prediction"])
            for r in self.results
        ) / len(self.results)

    def average_context_chunks(self):

        return sum(
            len(r["contexts"])
            for r in self.results
        ) / len(self.results)

    def average_context_size(self):

        total = 0

        for r in self.results:

            total += sum(
                len(chunk)
                for chunk in r["contexts"]
            )

        return total / len(self.results)

    def highest_confidence(self):

        return max(
            r["confidence"]
            for r in self.results
        )

    def lowest_confidence(self):

        return min(
            r["confidence"]
            for r in self.results
        )

    def low_confidence_answers(
        self,
        threshold=0.70
    ):

        return [

            r

            for r in self.results

            if r["confidence"] < threshold

        ]