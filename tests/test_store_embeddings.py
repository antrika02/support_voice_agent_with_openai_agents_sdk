from app.models import Document
from app.chunker import DocumentChunker
from app.retrieval.embeddings import EmbeddingGenerator
from app.retrieval.vector_store import VectorStore

from config import (
    QDRANT_URL,
    QDRANT_API_KEY,
    KNOWLEDGE_BASE_NAME,
    CRAWL_URL,
)

document = Document(
    title="Python Programming",
    content="""
Python is a high-level, interpreted programming language known for its simple syntax and readability.

Python supports object-oriented programming through classes and objects. Developers can create reusable classes, instantiate objects, use inheritance, encapsulation, and polymorphism to organize code effectively.

Python also supports functional programming using functions such as map(), filter(), lambda expressions, and comprehensions.

Python includes automatic memory management through reference counting and a garbage collector that frees unused memory automatically.

Because of its extensive standard library and large ecosystem, Python is widely used for web development, data science, artificial intelligence, automation, and scripting.
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
store.create_collection(
    vector_size=384
)

store.store_embeddings(
    chunks,
    embeddings
)

print("Done!")