from app.prompt_builder import PromptBuilder
from app.retriever import Retriever

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