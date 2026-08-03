from fastembed import TextEmbedding

from app.logging import get_logger
from app.models import Chunk


class EmbeddingGenerator:
    """
    Generates vector embeddings using FastEmbed.
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

        return self.embed_text(chunk.content)

    def embed_chunks(
        self,
        chunks: list[Chunk],
        batch_size: int = 32,
    ) -> list[list[float]]:
        """
        Generate embeddings in batches to avoid high memory usage.
        """

        if not chunks:
            return []

        self.logger.info(
            f"Generating embeddings for {len(chunks)} chunks."
        )

        all_embeddings = []

        for start in range(0, len(chunks), batch_size):

            end = min(start + batch_size, len(chunks))

            self.logger.info(
                f"Embedding batch {start // batch_size + 1} "
                f"({start}-{end-1})"
            )

            texts = [
                chunk.content
                for chunk in chunks[start:end]
            ]

            embeddings = self.model.embed(texts)

            all_embeddings.extend(
                embedding.tolist()
                for embedding in embeddings
            )

        self.logger.info(
            "Embedding generation complete."
        )

        return all_embeddings