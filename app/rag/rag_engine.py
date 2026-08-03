from app.llm.factory import LLMFactory
from app.logging import get_logger
from app.memory.conversation import Conversation
from app.rag.confidence import ConfidenceCalculator
from app.rag.prompt_builder import PromptBuilder
from app.response import (
    RAGResponse,
    Source,
)
from app.retrieval.retriever import Retriever
from config import MAX_CONVERSATION_MESSAGES


class RAGEngine:
    """
    Complete Retrieval-Augmented Generation (RAG) pipeline.

    Responsibilities:
    - Retrieve relevant documentation
    - Build the LLM prompt
    - Generate an answer
    - Calculate confidence
    - Build the final response
    """

    def __init__(self):
        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()
        self.llm = LLMFactory.create()
        self.logger = get_logger(__name__)

        self.conversation = Conversation(
            max_messages=MAX_CONVERSATION_MESSAGES
        )

    def answer(self, question: str) -> RAGResponse:
        """
        Answer a user's question using the RAG pipeline.
        """

        self.conversation.add_user_message(question)

        results = self.retriever.retrieve(question)

        if not results:

            self.logger.warning(
                "No relevant documents retrieved."
            )

            return RAGResponse(
                answer="I couldn't find relevant information in the documentation.",
                sources=[],
                confidence=0.0,
                contexts=[],
            )

        confidence = ConfidenceCalculator.calculate(results)

        prompt = self.prompt_builder.build(
            question=question,
            results=results,
            history=self.conversation.history(),
        )

        self.logger.info(
            f"Prompt length: {len(prompt)} characters"
        )

        contexts = self._extract_contexts(results)

        self.logger.info(
            f"Retrieved {len(contexts)} context chunks"
        )

        self.logger.info(
            f"Confidence score: {confidence:.2f}"
        )

        try:

            answer = self.llm.generate(prompt)

        except RuntimeError as e:

            self.logger.warning(str(e))

            answer = (
                "⚠️ Gemini is currently experiencing high demand.\n\n"
                "Please try again in a few moments."
            )

        self.conversation.add_assistant_message(answer)

        return RAGResponse(
            answer=answer,
            sources=self._extract_sources(results),
            confidence=confidence,
            contexts=contexts,
        )

    @staticmethod
    def _extract_contexts(results) -> list[str]:
        """
        Extract retrieved document contents.
        """

        return [
            result.payload.get("content", "")
            for result in results
        ]

    @staticmethod
    def _extract_sources(results) -> list[Source]:
        """
        Extract unique document sources.
        """

        sources = []
        seen_urls = set()

        for result in results:

            payload = result.payload

            url = payload.get("url")

            if not url or url in seen_urls:
                continue

            seen_urls.add(url)

            sources.append(
                Source(
                    title=payload.get("title") or "Unknown",
                    url=url,
                )
            )

        return sources