from app.embeddings import EmbeddingGenerator
from app.vector_store import VectorStore

from config import (
    QDRANT_URL,
    QDRANT_API_KEY,
    TOP_K,
    MIN_RETRIEVAL_SCORE,
)


class Retriever:
    """
    Retrieves relevant document chunks from Qdrant.
    """

    def __init__(self):
        self.embedder = EmbeddingGenerator()

        self.vector_store = VectorStore(
            QDRANT_URL,
            QDRANT_API_KEY
        )

        self.vector_store.connect()

    def retrieve(
        self,
        question: str,
        limit: int | None = None
    ):
        """
        Retrieve the most relevant chunks for a question.
        """

        if limit is None:
            limit = TOP_K

        question_embedding = self.embedder.embed_text(question)

        results = self.vector_store.search(
            question_embedding,
            limit=limit
        )

        filtered_results = []

    # Always keep the best result
        if results:
            filtered_results.append(results[0])

    # Filter the remaining results
        for result in results[1:]:

            if result.score >= MIN_RETRIEVAL_SCORE:
                filtered_results.append(result)

        return filtered_results