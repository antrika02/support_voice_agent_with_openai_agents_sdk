import re
import time

from firecrawl.v2.utils.error_handler import RateLimitError

from app.chunker import DocumentChunker
from app.ingestion.crawler import DocumentationCrawler
from app.ingestion.discovery import DocumentationDiscovery
from app.logging import get_logger
from app.retrieval.embeddings import EmbeddingGenerator
from app.retrieval.vector_store import VectorStore

from config import (
    QDRANT_API_KEY,
    QDRANT_URL,
)


class KnowledgeBaseManager:
    """
    Complete knowledge base ingestion pipeline.

    Flow:
    Discover -> Crawl -> Chunk -> Embed -> Store
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
            max_pages=10,
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

            max_retries = 3
            attempt = 0

            while attempt < max_retries:

                try:

                    documents.extend(
                        self.crawler.crawl_page(url)
                    )

                    break

                except RateLimitError as e:

                    attempt += 1

                    message = str(e)

                    match = re.search(
                        r"retry after (\d+)s",
                        message,
                        re.IGNORECASE,
                    )

                    wait_time = (
                        int(match.group(1))
                        if match
                        else 30
                    )

                    self.logger.warning(
                        f"Firecrawl rate limited. "
                        f"Retry {attempt}/{max_retries} "
                        f"after {wait_time} seconds."
                    )

                    time.sleep(wait_time + 1)

                except Exception as e:

                    self.logger.exception(
                        f"Failed to crawl {url}: {e}"
                    )

                    break

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
            "Connecting to Qdrant..."
        )

        self.vector_store.connect()

        # Temporary: remove the old collection once
        self.logger.info(
            "Deleting existing collection..."
        )

        self.vector_store.delete_collection()

        self.logger.info(
            "Creating collection..."
        )

        self.vector_store.create_collection(
            vector_size=len(embeddings[0]),
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