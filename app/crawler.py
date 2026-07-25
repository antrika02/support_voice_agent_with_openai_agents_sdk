from firecrawl import FirecrawlApp

from app.models import Document
from config import FIRECRAWL_API_KEY


class DocumentationCrawler:

    def __init__(self):
        self.client = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

    def crawl(self, url: str) -> list[Document]:
        """
        Crawl a documentation page and return Document objects.
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