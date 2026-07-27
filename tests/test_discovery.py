from app.ingestion.discovery import DocumentationDiscovery

from config import CRAWL_URL

discovery = DocumentationDiscovery()

urls = discovery.discover(
    CRAWL_URL,
    max_pages=20
)

print(f"Found {len(urls)} pages\n")

for url in urls:
    print(url)