from app.ingestion.crawler import DocumentationCrawler

crawler = DocumentationCrawler()

from config import CRAWL_URL

docs = crawler.crawl(CRAWL_URL)
print(docs[0].title)
print(docs[0].url)
print(docs[0].content[:500])