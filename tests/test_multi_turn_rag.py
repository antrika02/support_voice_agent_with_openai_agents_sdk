from app.rag.rag_engine import RAGEngine

rag = RAGEngine()

questions = [
    "What is Python?",
    "How does it support object-oriented programming?",
    "What about functional programming?"
]

for question in questions:
    print("=" * 80)
    print("QUESTION:")
    print(question)

    answer = rag.answer(question)

    print()
    print("ANSWER:")
    print(answer)
    print("=" * 80)