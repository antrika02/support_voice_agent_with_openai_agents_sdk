from app.models import Document
from app.chunker import DocumentChunker

doc = Document(
    title="Python",
    content="""
Python is easy to learn. It supports object-oriented programming.
It supports functional programming.
Python has automatic memory management.
It has a huge ecosystem.
""",
    url="https://python.org"
)

chunker = DocumentChunker(chunk_size=2, overlap=1)

chunks = chunker.chunk_document(doc)

for chunk in chunks:
    print("-" * 40)
    print(chunk.chunk_number)
    print(chunk.content)