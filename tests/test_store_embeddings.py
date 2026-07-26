from app.models import Document
from app.chunker import DocumentChunker
from app.embeddings import EmbeddingGenerator
from app.vector_store import VectorStore

from config import (
    QDRANT_URL,
    QDRANT_API_KEY,
)

document = Document(
    title="Python",
    content="""
Python is easy to learn.
Python supports OOP.
Python supports functional programming.
Python has automatic memory management.
Python has a huge ecosystem.
""",
    url="https://python.org"
)

chunker = DocumentChunker()

chunks = chunker.chunk_document(document)

embedder = EmbeddingGenerator()

embeddings = embedder.embed_chunks(chunks)

store = VectorStore(
    QDRANT_URL,
    QDRANT_API_KEY
)

store.connect()

store.store_embeddings(
    chunks,
    embeddings
)

print("Done!")