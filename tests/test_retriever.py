from app.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve(
    "How does Python support object-oriented programming?"
)

print("=" * 60)

for result in results:

    print("Score:", result.score)

    print(result.payload["content"])

    print("=" * 60)