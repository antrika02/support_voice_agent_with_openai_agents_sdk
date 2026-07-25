from app.crawler import DocumentationCrawler

crawler = DocumentationCrawler()

docs = crawler.crawl(
    "https://docs.python.org/3/tutorial/introduction.html"
)

print(docs[0].title)
print(docs[0].url)
print(docs[0].content[:500])