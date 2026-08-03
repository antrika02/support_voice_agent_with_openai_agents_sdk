from typing import Any


SYSTEM_PROMPT = """
You are an expert documentation assistant.

Answer the user's question using ONLY the documentation below.

Use the conversation history to understand follow-up questions.

If the documentation contains enough information to answer the question,
write a concise, accurate, and helpful answer.

Do not use outside knowledge.

If the documentation is clearly unrelated to the user's question,
respond ONLY with:

"I couldn't find that information in the documentation."

Conversation History
--------------------
{history}

Documentation
--------------------
{documentation}
--------------------

Current Question:
{question}

Answer:
""".strip()


class PromptBuilder:
    """
    Builds prompts for the language model using retrieved context.
    """

    def build(
        self,
        question: str,
        results: list[Any],
        history: list[Any] | None = None,
    ) -> str:
        """
        Build a prompt for the language model using
        conversation history and retrieved documentation.
        """

        history_text = self._build_history(history)

        documentation = "\n\n".join(
            result.payload.get("content", "")
            for result in results
        )

        return SYSTEM_PROMPT.format(
            history=history_text,
            documentation=documentation,
            question=question,
        )

    @staticmethod
    def _build_history(
        history: list[Any] | None,
    ) -> str:
        """
        Convert conversation history into prompt text.
        """

        if not history:
            return ""

        return "\n".join(
            f"{message.role.capitalize()}: {message.content}"
            for message in history
        )