from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """
    Abstract base class for all LLM providers.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate an answer from a prompt.
        """
        pass