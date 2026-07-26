from app.retriever import Retriever
from app.prompt_builder import PromptBuilder
from app.llm.factory import LLMFactory


class RAGEngine:
    """
    Complete Retrieval-Augmented Generation pipeline.
    """

    def __init__(self):
        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()
        self.llm = LLMFactory.create()

    def answer(self, question: str) -> str:
        """
        Answer a user's question using RAG.
        """

        results = self.retriever.retrieve(question)

        prompt = self.prompt_builder.build(
            question,
            results
        )

        response = self.llm.generate(prompt)

        return response