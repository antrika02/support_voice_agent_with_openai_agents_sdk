from app.llm.factory import LLMFactory

llm = LLMFactory.create()

print(type(llm).__name__)