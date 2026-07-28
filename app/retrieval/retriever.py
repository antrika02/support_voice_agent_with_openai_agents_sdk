from typing import Any

from app.logging import get_logger
from app.retrieval.embeddings import EmbeddingGenerator
from app.retrieval.vector_store import VectorStore

from config import (
    MIN_RETRIEVAL_SCORE,
    QDRANT_API_KEY,
    QDRANT_URL,
    TOP_K,
)


class Retriever:
    """
    Retrieves the most relevant document chunks from the vector store.

    Responsibilities:
    - Generate an embedding for the user's question.
    - Search Qdrant for similar document chunks.
    - Filter low-confidence matches while always preserving the
      highest-ranked result.
    """

    def __init__(self):
        self.embedder = EmbeddingGenerator()

        self.vector_store = VectorStore(
            QDRANT_URL,
            QDRANT_API_KEY,
        )

        self.vector_store.connect()

        self.logger = get_logger(__name__)

    def retrieve(
        self,
        question: str,
        limit: int | None = None,
    ) -> list[Any]:
        """
        Retrieve the most relevant document chunks.

        Args:
            question: User's query.
            limit: Maximum number of results to retrieve.

        Returns:
            Filtered list of retrieved document chunks.
        """

        if not question.strip():

            self.logger.warning(
                "Received an empty retrieval query."
            )

            return []

        limit = limit or TOP_K

        self.logger.info(
            f"Retrieving top {limit} documents."
        )

        question_embedding = self.embedder.embed_text(
            question
        )

        results = self.vector_store.search(
            question_embedding,
            limit=limit,
        )

        self.logger.info(
            f"Retrieved {len(results)} candidate chunks."
        )

        if not results:
            return []

        filtered_results = [results[0]]

        filtered_results.extend(
            result
            for result in results[1:]
            if result.score >= MIN_RETRIEVAL_SCORE
        )

        self.logger.info(
            f"{len(filtered_results)} chunks remained after filtering."
        )

        return filtered_results