from google import genai

from app.llm.base import BaseLLM

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
)


class GeminiLLM(BaseLLM):
    """
    Gemini implementation of the LLM interface.
    """

    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )

        return response.text