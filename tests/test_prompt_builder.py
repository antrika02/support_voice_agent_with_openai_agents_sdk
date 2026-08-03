from app.rag.prompt_builder import PromptBuilder
from app.retrieval.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve(
    "How does Python support object-oriented programming?"
)

builder = PromptBuilder()

prompt = builder.build(
    "How does Python support object-oriented programming?",
    results
)

print(prompt)