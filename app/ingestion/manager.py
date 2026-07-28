from app.ingestion.discovery import DocumentationDiscovery
from app.ingestion.crawler import DocumentationCrawler
from app.chunker import DocumentChunker
from app.retrieval.embeddings import EmbeddingGenerator
from app.retrieval.vector_store import VectorStore

from config import (
    CRAWL_URL,
    QDRANT_URL,
    QDRANT_API_KEY,
)


class KnowledgeBaseManager:
    """
    Complete knowledge base ingestion pipeline.
    """

    def __init__(self):

        self.discovery = DocumentationDiscovery()

        self.crawler = DocumentationCrawler()

        self.chunker = DocumentChunker()

        self.embedder = EmbeddingGenerator()

        self.vector_store = VectorStore(
            QDRANT_URL,
            QDRANT_API_KEY
        )

        self.vector_store.connect()

    def ingest(self, crawl_url: str):
        """
        Discover → Crawl → Chunk → Embed → Store
        """

        print("Step 1: Discovering documentation pages...")

        urls = self.discovery.discover(
            crawl_url,
            max_pages=50
        )

        print(f"Discovered {len(urls)} pages.")

        documents = []

        print("Step 2: Crawling pages...")

        for index, url in enumerate(urls, start=1):

            print(f"[{index}/{len(urls)}] {url}")

            try:

                documents.extend(
                    self.crawler.crawl_page(url)
                )

            except Exception as e:

                print(f"Failed: {e}")

        print(f"Crawled {len(documents)} document(s).")

        chunks = []

        print("Step 3: Chunking...")

        for document in documents:

            chunks.extend(
                self.chunker.chunk_document(document)
            )

        print(f"Created {len(chunks)} chunk(s).")

        print("Step 4: Generating embeddings...")

        embeddings = self.embedder.embed_chunks(chunks)

        print("Step 5: Creating collection...")

        self.vector_store.create_collection(
            vector_size=384
        )

        print("Step 6: Uploading to Qdrant...")

        self.vector_store.store_embeddings(
            chunks,
            embeddings
        )

        print("Knowledge base successfully indexed.")