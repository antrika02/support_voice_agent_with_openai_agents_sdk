from app.rag.rag_engine import RAGEngine

rag = RAGEngine()

response = rag.answer(
    "How does Python support object-oriented programming?"
)

print("=" * 80)
print("CONTEXTS")
print("=" * 80)

for i, context in enumerate(response.contexts, start=1):
    print(f"\nContext {i}")
    print("-" * 40)
    print(context[:300])

print("=" * 80)
print("NUMBER OF CONTEXTS:", len(response.contexts))