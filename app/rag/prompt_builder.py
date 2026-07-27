class PromptBuilder:
    """
    Builds prompts for the language model using retrieved context.
    """

    def build(
        self,
        question: str,
        results,
        history=None
    ):
        """
        Build a RAG prompt from retrieved Qdrant results.
        """

        # -----------------------------
        # Build conversation history
        # -----------------------------
        history_text = ""

        if history:
            for message in history:
                history_text += (
                    f"{message.role.capitalize()}: "
                    f"{message.content}\n"
                )

        # -----------------------------
        # Build documentation context
        # -----------------------------
        context = []

        for result in results:
            context.append(result.payload["content"])

        documentation = "\n\n".join(context)

        # -----------------------------
        # Final prompt
        # -----------------------------
        prompt = f"""
You are an expert documentation assistant.

Answer the user's question using ONLY the documentation below.

Use the conversation history to understand follow-up questions.

If the documentation contains enough information to answer the question,
write a concise, accurate, and helpful answer.

Do not use outside knowledge.

Only respond with:

"I couldn't find that information in the documentation."

if the documentation is clearly unrelated to the user's question.

Conversation History
--------------------
{history_text}

Documentation
--------------------
{documentation}
--------------------

Current Question:
{question}

Answer:
"""

        return prompt