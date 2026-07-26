from app.llm.factory import LLMFactory

llm = LLMFactory.create()

response = llm.generate(
    "In one sentence, explain what Python is."
)

print(response)