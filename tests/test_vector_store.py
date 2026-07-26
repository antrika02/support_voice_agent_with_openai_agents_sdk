from config import (
    QDRANT_URL,
    QDRANT_API_KEY,
)

from app.vector_store import VectorStore

store = VectorStore(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

store.connect()

store.create_collection(vector_size=384)

print("Setup Complete!")