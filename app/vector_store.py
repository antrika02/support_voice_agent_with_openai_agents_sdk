from qdrant_client import QdrantClient


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

    def create_collection(self):
        """Create a collection if it doesn't exist."""
        pass

    def store_embeddings(self):
        """Store embeddings in Qdrant."""
        pass

    def search(self):
        """Search for similar embeddings."""
        pass

    def delete_collection(self):
        """Delete a collection."""
        pass