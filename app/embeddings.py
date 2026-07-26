from fastembed import TextEmbedding

from app.models import Chunk


class EmbeddingGenerator:
    """
    Generates embeddings for document chunks.
    """

    def __init__(self):
        self.model = TextEmbedding()

    def embed_text(self, text: str):
        """
        Generate an embedding for any text.
        """
        embedding = list(self.model.embed([text]))[0]
        return embedding.tolist()

    def embed_chunk(self, chunk: Chunk):
        """
        Generate an embedding for a single chunk.
        """
        embedding = list(self.model.embed([chunk.content]))[0]
        return embedding.tolist()

    def embed_chunks(self, chunks: list[Chunk]):
        """
        Generate embeddings for multiple chunks.
        """
        embeddings = []

        for chunk in chunks:
            vector = self.embed_chunk(chunk)
            embeddings.append(vector)

        return embeddings