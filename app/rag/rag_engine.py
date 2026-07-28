from app.retrieval.retriever import Retriever
from app.rag.prompt_builder import PromptBuilder
from app.llm.factory import LLMFactory
from app.memory.conversation import Conversation
from app.rag.confidence import ConfidenceCalculator
from config import MAX_CONVERSATION_MESSAGES
from app.response import (
    Source,
    RAGResponse,
)


class RAGEngine:
    """
    Complete Retrieval-Augmented Generation pipeline.
    """

    def __init__(self):
        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()
        self.llm = LLMFactory.create()

        self.conversation = Conversation(
            max_messages=MAX_CONVERSATION_MESSAGES
        )

    def answer(self, question: str) -> RAGResponse:
        """
        Answer a user's question using RAG.
        """

        self.conversation.add_user_message(question)

        results = self.retriever.retrieve(question)

        confidence = ConfidenceCalculator.calculate(results)

        prompt = self.prompt_builder.build(
            question=question,
            results=results,
            history=self.conversation.history()
        )

        print("=" * 80)
        print(f"Prompt length: {len(prompt)} characters")
        print("=" * 80)

        answer = self.llm.generate(prompt)

        contexts = [
            result.payload["content"]
            for result in results
        ]

        self.conversation.add_assistant_message(answer)

        sources = []

        seen_urls = set()

        for result in results:

            url = result.payload["url"]

            if url in seen_urls:
                continue

            seen_urls.add(url)

            sources.append(
                Source(
                    title=result.payload["title"],
                    url=url
                )
            )

        return RAGResponse(
            answer=answer,
            sources=sources,
            confidence=confidence,
            contexts=contexts,
        )