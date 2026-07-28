import time

from google import genai
from google.genai.errors import (
    ClientError,
    ServerError,
)

from app.llm.base import BaseLLM
from app.logging import get_logger

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
)

logger = get_logger(__name__)


class GeminiLLM(BaseLLM):

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.model = GEMINI_MODEL

    def generate(self, prompt: str) -> str:

        retries = 3

        for attempt in range(retries):

            try:

                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt,
                )

                return response.text

            except ServerError:

                logger.warning(
                    f"Gemini unavailable ({attempt+1}/{retries})"
                )

                if attempt < retries - 1:
                    time.sleep(2)
                    continue

                raise RuntimeError(
                    "Gemini service temporarily unavailable."
                )

            except ClientError:
                raise

            except Exception:
                raise