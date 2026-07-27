from firecrawl import FirecrawlApp

from app.models import Document
from config import FIRECRAWL_API_KEY


class DocumentationCrawler:
    """
    Crawls a single documentation page and converts it into a Document.
    """

    def __init__(self):
        self.client = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

    def crawl_page(self, url: str) -> list[Document]:
        """
        Crawl a single documentation page.
        """

        response = self.client.scrape_url(url)

        markdown = getattr(response, "markdown", "")
        metadata = getattr(response, "metadata", {})

        document = Document(
            title=getattr(metadata, "title", ""),
            content=markdown,
            url=getattr(metadata, "sourceURL", url),
            description=getattr(metadata, "description", ""),
            language=getattr(metadata, "language", "en"),
            metadata={}
        )

        return [document]