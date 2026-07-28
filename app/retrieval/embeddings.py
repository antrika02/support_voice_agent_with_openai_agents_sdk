from fastembed import TextEmbedding

from app.logging import get_logger
from app.models import Chunk


class EmbeddingGenerator:
    """
    Generates vector embeddings using FastEmbed.

    Responsibilities:
    - Embed individual text
    - Embed document chunks
    - Batch embed multiple chunks efficiently
    """

    def __init__(self):
        self.logger = get_logger(__name__)

        self.logger.info(
            "Loading FastEmbed model..."
        )

        self.model = TextEmbedding()

    def embed_text(
        self,
        text: str,
    ) -> list[float]:
        """
        Generate an embedding for arbitrary text.
        """

        if not text.strip():
            return []

        embedding = next(
            self.model.embed([text])
        )

        return embedding.tolist()

    def embed_chunk(
        self,
        chunk: Chunk,
    ) -> list[float]:
        """
        Generate an embedding for a single chunk.
        """

        return self.embed_text(chunk.content)

    def embed_chunks(
        self,
        chunks: list[Chunk],
    ) -> list[list[float]]:
        """
        Generate embeddings for multiple chunks in a single batch.

        FastEmbed performs significantly better when embedding
        batches instead of one document at a time.
        """

        if not chunks:
            return []

        self.logger.info(
            f"Generating embeddings for {len(chunks)} chunks."
        )

        texts = [
            chunk.content
            for chunk in chunks
        ]

        embeddings = self.model.embed(texts)

        return [
            embedding.tolist()
            for embedding in embeddings
        ]