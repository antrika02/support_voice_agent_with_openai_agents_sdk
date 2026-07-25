from app.models import Document, Chunk
import uuid


class DocumentChunker:

    def __init__(self, chunk_size=2, overlap=1):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_document(self, document: Document) -> list[Chunk]:

        text = document.content.replace("\n", " ")

        sentences = text.split(". ")

        chunks = []

        step = self.chunk_size - self.overlap

        if step <= 0:
            raise ValueError("Overlap must be smaller than chunk size.")

        for i in range(0, len(sentences), step):

            current_sentences = sentences[i:i + self.chunk_size]

            if not current_sentences:
                continue

            content = ". ".join(current_sentences)

            chunk = Chunk(
                id=str(uuid.uuid4()),
                content=content,
                source_url=document.url,
                document_title=document.title,
                chunk_number=len(chunks) + 1
            )

            chunks.append(chunk)

        return chunks