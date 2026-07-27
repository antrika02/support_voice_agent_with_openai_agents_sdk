from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from qdrant_client.models import PointStruct

import uuid

from config import (
    COLLECTION_NAME,
    UPSERT_BATCH_SIZE,
)

from app.models import Chunk


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
            api_key=self.api_key,
        )

        return self.client

    def create_collection(self, vector_size: int):
        """
        Create the collection if it does not already exist.
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
                distance=Distance.COSINE,
            ),
        )

        print(f"Collection '{COLLECTION_NAME}' created successfully!")

    def store_embeddings(
        self,
        chunks: list[Chunk],
        embeddings: list[list[float]],
    ):
        """
        Store chunk embeddings inside Qdrant using batched uploads.
        """

        points = []

        for chunk, embedding in zip(chunks, embeddings):

            point = PointStruct(
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

            points.append(point)

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

            print(
                f"Uploading batch "
                f"{batch_number + 1}/{total_batches} "
                f"({len(batch)} vectors)"
            )

            self.client.upsert(
                collection_name=COLLECTION_NAME,
                points=batch,
            )

        print(f"\nStored {len(points)} embeddings.")

    def search(
        self,
        query_embedding: list[float],
        limit: int = 3,
    ):
        """
        Search for similar document chunks.
        """

        results = self.client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_embedding,
            limit=limit,
        )

        return results.points

    def delete_collection(self):
        """
        Delete the collection if it exists.
        """

        collections = self.client.get_collections().collections

        existing_collections = [
            c.name for c in collections
        ]

        if COLLECTION_NAME in existing_collections:

            self.client.delete_collection(
                collection_name=COLLECTION_NAME,
            )

            print(f"Deleted '{COLLECTION_NAME}'.")

        else:

            print("Collection does not exist.")