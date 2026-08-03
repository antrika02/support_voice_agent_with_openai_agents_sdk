from app.retrieval.vector_store import VectorStore

from config import (
    QDRANT_URL,
    QDRANT_API_KEY,
    COLLECTION_NAME,
)


class MetricsService:

    def __init__(self):

        self.store = VectorStore(
            QDRANT_URL,
            QDRANT_API_KEY
        )

        self.store.connect()

    def get_metrics(self):

        info = self.store.client.get_collection(
            COLLECTION_NAME
        )

        return {
            "collection": COLLECTION_NAME,
            "vectors": info.points_count,
            "status": info.status,
        }