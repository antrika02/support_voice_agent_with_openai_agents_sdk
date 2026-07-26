from app.llm.gemini import GeminiLLM


class LLMFactory:

    @staticmethod
    def create():

        return GeminiLLM()