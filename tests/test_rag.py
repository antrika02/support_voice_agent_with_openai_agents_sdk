from app.rag.rag_engine import RAGEngine

rag = RAGEngine()

question = "How does Python support object-oriented programming?"

answer = rag.answer(question)

print("=" * 60)
print("QUESTION:")
print(question)

print("\nANSWER:")
print(answer)
print("=" * 60)