from app.ingestion.manager import KnowledgeBaseManager

manager = KnowledgeBaseManager()

manager.ingest(
    "https://docs.stripe.com"
)