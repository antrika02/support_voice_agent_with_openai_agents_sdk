from config import QDRANT_URL, QDRANT_API_KEY
from app.vector_store import VectorStore

store = VectorStore(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

client = store.connect()

print("✅ Connected to Qdrant!")

collections = client.get_collections()

print(collections)