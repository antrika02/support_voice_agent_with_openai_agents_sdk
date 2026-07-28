from evaluation.metrics import EvaluationMetrics


metrics = EvaluationMetrics()

print("=" * 60)
print("Enterprise RAG Evaluation Report")
print("=" * 60)

print()

print(f"Questions Evaluated : {len(metrics.results)}")

print(
    f"Average Confidence : "
    f"{metrics.average_confidence():.2f}"
)

print(
    f"Average Answer Length : "
    f"{metrics.average_answer_length():.1f}"
)

print(
    f"Average Context Chunks : "
    f"{metrics.average_context_chunks():.1f}"
)

print(
    f"Average Context Size : "
    f"{metrics.average_context_size():.1f}"
)

print()

print(
    f"Highest Confidence : "
    f"{metrics.highest_confidence():.2f}"
)

print(
    f"Lowest Confidence : "
    f"{metrics.lowest_confidence():.2f}"
)

print()

print(
    f"Low Confidence Answers : "
    f"{len(metrics.low_confidence_answers())}"
)

print("=" * 60)