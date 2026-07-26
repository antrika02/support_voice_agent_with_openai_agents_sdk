from app.rag_engine import RAGEngine

rag = RAGEngine()

print("=" * 80)
print("Customer Support Chat")
print("Type 'exit' to quit.")
print("=" * 80)

while True:
    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        break

    answer = rag.answer(question)

    print(f"\nAssistant: {answer}")