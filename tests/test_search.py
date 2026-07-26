from app.embeddings import EmbeddingGenerator
from app.vector_store import VectorStore

from config import (
    QDRANT_URL,
    QDRANT_API_KEY,
)

question = "How does Python support OOP?"

embedder = EmbeddingGenerator()

question_embedding = embedder.embed_text(question)

store = VectorStore(
    QDRANT_URL,
    QDRANT_API_KEY
)

store.connect()

results = store.search(question_embedding)

print("=" * 60)

for result in results:

    print("Score:", result.score)

    print(result.payload["content"])

    print("=" * 60)