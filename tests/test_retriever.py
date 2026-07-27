from app.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve(
    "How does Python support object-oriented programming?"
)

print("=" * 80)

print(f"Retrieved {len(results)} chunks")

print("=" * 80)

for result in results:
    print(f"Score: {result.score:.4f}")
    print(result.payload["content"])
    print("-" * 80)