from app.rag_engine import RAGEngine

rag = RAGEngine()

response = rag.answer(
    "How does Python support object-oriented programming?"
)

print("=" * 80)
print("ANSWER")
print("=" * 80)

print(response.answer)

print()

print("CONFIDENCE")
print("=" * 80)

print(f"{response.confidence:.2%}")

print()

print("SOURCES")
print("=" * 80)

for source in response.sources:
    print(source.title)
    print(source.url)