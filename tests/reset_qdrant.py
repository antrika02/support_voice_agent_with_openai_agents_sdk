from app.retrieval.vector_store import VectorStore
from config import QDRANT_URL, QDRANT_API_KEY

store = VectorStore(
    QDRANT_URL,
    QDRANT_API_KEY
)

store.connect()

store.delete_collection()

print("Collection deleted.")