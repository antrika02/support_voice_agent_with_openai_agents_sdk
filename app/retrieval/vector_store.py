import uuid

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from qdrant_client.models import PointStruct

from app.logging import get_logger
from app.models import Chunk

from config import (
    COLLECTION_NAME,
    UPSERT_BATCH_SIZE,
)


class VectorStore:
    """
    Handles all interaction with Qdrant.

    Responsibilities:
    - Connect to Qdrant
    - Create/Delete collections
    - Store embeddings
    - Retrieve relevant chunks
    """

    def __init__(
        self,
        url: str,
        api_key: str,
    ):
        self.url = url
        self.api_key = api_key
        self.client: QdrantClient | None = None

        self.logger = get_logger(__name__)

    def connect(self) -> QdrantClient:
        """
        Establish a connection to Qdrant.
        """

        if self.client is None:

            self.logger.info(
                "Connecting to Qdrant..."
            )

            self.client = QdrantClient(
                url=self.url,
                api_key=self.api_key,
            )

            self.logger.info(
                "Connected to Qdrant."
            )

        return self.client

    def create_collection(
        self,
        vector_size: int,
    ) -> None:
        """
        Create the collection if it does not already exist.
        """

        collections = self.client.get_collections().collections

        existing = {
            collection.name
            for collection in collections
        }

        if COLLECTION_NAME in existing:

            self.logger.info(
                f"Collection '{COLLECTION_NAME}' already exists."
            )

            return

        self.client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )

        self.logger.info(
            f"Collection '{COLLECTION_NAME}' created."
        )

    def store_embeddings(
        self,
        chunks: list[Chunk],
        embeddings: list[list[float]],
    ) -> None:
        """
        Store embeddings in Qdrant using batched uploads.
        """

        if not chunks:

            self.logger.warning(
                "No chunks provided for indexing."
            )

            return

        if len(chunks) != len(embeddings):

            raise ValueError(
                "Chunks and embeddings must have the same length."
            )

        points = []

        for chunk, embedding in zip(chunks, embeddings):

            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=embedding,
                    payload={
                        "id": chunk.id,
                        "title": chunk.document_title,
                        "content": chunk.content,
                        "url": chunk.source_url,
                        "chunk_number": chunk.chunk_number,
                        "metadata": chunk.metadata,
                    },
                )
            )

        total_batches = (
            len(points) + UPSERT_BATCH_SIZE - 1
        ) // UPSERT_BATCH_SIZE

        for batch_number in range(total_batches):

            start = batch_number * UPSERT_BATCH_SIZE

            end = min(
                start + UPSERT_BATCH_SIZE,
                len(points),
            )

            batch = points[start:end]

            self.logger.info(
                f"Uploading batch "
                f"{batch_number + 1}/{total_batches} "
                f"({len(batch)} vectors)"
            )

            self.client.upsert(
                collection_name=COLLECTION_NAME,
                points=batch,
            )

        self.logger.info(
            f"Stored {len(points)} embeddings."
        )

    def search(
        self,
        query_embedding: list[float],
        limit: int = 3,
    ):
        """
        Search for the most relevant document chunks.
        """

        self.logger.info(
            f"Searching top {limit} chunks."
        )

        results = self.client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_embedding,
            limit=limit,
        )

        self.logger.info(
            f"Retrieved {len(results.points)} chunks."
        )

        return results.points

    def delete_collection(self) -> None:
        """
        Delete the collection if it exists.
        """

        collections = self.client.get_collections().collections

        existing = {
            collection.name
            for collection in collections
        }

        if COLLECTION_NAME not in existing:

            self.logger.info(
                "Collection does not exist."
            )

            return

        self.client.delete_collection(
            collection_name=COLLECTION_NAME,
        )

        self.logger.info(
            f"Deleted '{COLLECTION_NAME}'."
        )