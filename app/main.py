from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="AI Documentation Assistant",
    version="1.0.0",
    description="Conversational RAG API powered by Gemini and Qdrant."
)

app.include_router(router)