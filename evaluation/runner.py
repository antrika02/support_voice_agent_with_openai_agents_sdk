import json

from google.genai.errors import ClientError

from app.evaluation.models import EvaluationResult
from app.rag.rag_engine import RAGEngine
from evaluation.reporter import EvaluationReporter


class EvaluationRunner:

    def __init__(self):

        self.rag = RAGEngine()

        self.reporter = EvaluationReporter()

    def load_dataset(self, path):

        with open(path, "r") as f:
            return json.load(f)

    def evaluate(self, path):

        dataset = self.load_dataset(path)

        completed = self.reporter.load_existing()

        completed_questions = {
            item["question"]
            for item in completed
        }

        for sample in dataset:

            if sample["question"] in completed_questions:

                print(
                    f"Skipping: {sample['question']}"
                )

                continue

            print("=" * 70)
            print(sample["question"])

            try:

                response = self.rag.answer(
                    sample["question"]
                )

                result = EvaluationResult(
                    question=sample["question"],
                    ground_truth=sample["ground_truth"],
                    prediction=response.answer,
                    contexts=response.contexts,
                    sources=response.sources,
                    confidence=response.confidence,
                )

                self.reporter.save_result(
                    result
                )

                print("Saved")

            except ClientError as e:

                print("\nGemini quota exceeded.")
                print("Progress saved.")
                print("Resume later.\n")

                break