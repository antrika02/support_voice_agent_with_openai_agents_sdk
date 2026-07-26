from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

from config import COLLECTION_NAME

class VectorStore:
    """
    Handles storage and retrieval of embeddings in Qdrant.
    """

    def __init__(self, url: str, api_key: str):
        self.url = url
        self.api_key = api_key
        self.client = None

    def connect(self):
        """
        Establish a connection to Qdrant.
        """
        self.client = QdrantClient(
            url=self.url,
            api_key=self.api_key
        )

        return self.client

    def create_collection(self, vector_size: int):
        """
        Creates the collection if it doesn't already exist.
        """

        collections = self.client.get_collections().collections

        existing_collections = [c.name for c in collections]

        if COLLECTION_NAME in existing_collections:
            print(f"Collection '{COLLECTION_NAME}' already exists.")
            return

        self.client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
        )
    )

    print(f"Collection '{COLLECTION_NAME}' created successfully!")

    def store_embeddings(self):
        """Store embeddings in Qdrant."""
        pass

    def search(self):
        """Search for similar embeddings."""
        pass

    def delete_collection(self):
        """Delete a collection."""
        pass