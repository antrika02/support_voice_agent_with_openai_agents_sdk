from app.ingestion.discovery import DocumentationDiscovery
from app.ingestion.crawler import DocumentationCrawler
from app.chunker import DocumentChunker
from app.retrieval.embeddings import EmbeddingGenerator
from app.retrieval.vector_store import VectorStore
from app.logging import get_logger

from config import (
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
            QDRANT_API_KEY,
        )

        self.vector_store.connect()

        self.logger = get_logger(__name__)

    def ingest(self, crawl_url: str):
        """
        Discover → Crawl → Chunk → Embed → Store
        """

        self.logger.info(
            "Discovering documentation pages..."
        )

        urls = self.discovery.discover(
            crawl_url,
            max_pages=50,
        )

        self.logger.info(
            f"Discovered {len(urls)} pages."
        )

        documents = []

        self.logger.info(
            "Crawling documentation pages..."
        )

        for index, url in enumerate(urls, start=1):

            self.logger.info(
                f"[{index}/{len(urls)}] {url}"
            )

            try:

                documents.extend(
                    self.crawler.crawl_page(url)
                )

            except Exception as e:

                self.logger.exception(
                    f"Failed to crawl {url}: {e}"
                )

        self.logger.info(
            f"Crawled {len(documents)} documents."
        )

        chunks = []

        self.logger.info(
            "Chunking documents..."
        )

        for document in documents:

            chunks.extend(
                self.chunker.chunk_document(document)
            )

        self.logger.info(
            f"Created {len(chunks)} chunks."
        )

        self.logger.info(
            "Generating embeddings..."
        )

        embeddings = self.embedder.embed_chunks(chunks)

        self.logger.info(
            "Creating collection..."
        )

        self.vector_store.create_collection(
            vector_size=384
        )

        self.logger.info(
            "Uploading embeddings..."
        )

        self.vector_store.store_embeddings(
            chunks,
            embeddings,
        )

        self.logger.info(
            "Knowledge base successfully indexed."
        )