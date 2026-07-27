import time

from google import genai
from google.genai.errors import ServerError

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

    def generate(
        self,
        prompt: str,
        retries: int = 3,
        delay: int = 2,
    ) -> str:
        """
        Generate a response using Gemini with automatic retries.
        """

        for attempt in range(retries):

            try:

                response = self.client.models.generate_content(
                    model=GEMINI_MODEL,
                    contents=prompt,
                )

                return response.text

            except ServerError as e:

                print(
                    f"Gemini temporarily unavailable "
                    f"(Attempt {attempt + 1}/{retries})"
                )

                if attempt == retries - 1:
                    raise e

                time.sleep(delay)

        raise RuntimeError("Unexpected error while calling Gemini.")