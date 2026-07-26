from app.retriever import Retriever
from app.prompt_builder import PromptBuilder
from app.llm.factory import LLMFactory
from app.memory.conversation import Conversation

from config import MAX_CONVERSATION_MESSAGES


class RAGEngine:
    """
    Complete Retrieval-Augmented Generation pipeline.
    """

    def __init__(self):
        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()
        self.llm = LLMFactory.create()

        self.conversation = Conversation(
            max_messages=MAX_CONVERSATION_MESSAGES
        )

    def answer(self, question: str) -> str:
        self.conversation.add_user_message(question)

        results = self.retriever.retrieve(question)

        prompt = self.prompt_builder.build(
            question=question,
            results=results,
            history=self.conversation.history()
        )

        print("=" * 80)
        print(prompt)
        print("=" * 80)

        response = self.llm.generate(prompt)

        self.conversation.add_assistant_message(response)

        return response