from app.embeddings import EmbeddingGenerator
from app.vector_store import VectorStore

from config import (
    QDRANT_URL,
    QDRANT_API_KEY,
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
        limit: int = 3
    ):
        """
        Retrieve the most relevant chunks for a question.
        """

        question_embedding = self.embedder.embed_text(question)

        results = self.vector_store.search(
            question_embedding,
            limit=limit
        )

        return results