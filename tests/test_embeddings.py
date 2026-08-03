from app.models import Chunk
from app.retrieval.embeddings import EmbeddingGenerator

chunk = Chunk(
    id="1",
    content="Python is an easy programming language.",
    source_url="https://python.org",
    document_title="Python",
    chunk_number=1,
)

generator = EmbeddingGenerator()

embedding = generator.embed_chunk(chunk)

print(type(embedding))
print(len(embedding))
print(embedding[:10])