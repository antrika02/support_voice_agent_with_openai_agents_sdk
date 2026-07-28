import json
import os
from dataclasses import asdict


class EvaluationReporter:

    def __init__(self):
        self.output_path = "evaluation/results.json"

    def load_existing(self):

        if not os.path.exists(self.output_path):
            return []

        with open(self.output_path, "r") as f:
            return json.load(f)

    def save_result(self, result):

        results = self.load_existing()

        results.append(
            asdict(result)
        )

        with open(self.output_path, "w") as f:

            json.dump(
                results,
                f,
                indent=4,
            )

    def save_all(self, results):

        with open(self.output_path, "w") as f:

            json.dump(
                [asdict(r) for r in results],
                f,
                indent=4,
            )