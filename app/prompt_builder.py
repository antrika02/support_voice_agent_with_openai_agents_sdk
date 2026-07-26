class PromptBuilder:
    """
    Builds prompts for the language model using retrieved context.
    """

    def build(self, question: str, results):
        """
        Build a RAG prompt from retrieved Qdrant results.
        """

        context = []

        for result in results:
            context.append(result.payload["content"])

        documentation = "\n\n".join(context)

        prompt = f"""
You are an expert documentation assistant.

Use ONLY the documentation below to answer the user's question.

If the documentation does not contain the answer, say:

"I couldn't find that information in the documentation."

Documentation:
--------------------
{documentation}
--------------------

Question:
{question}

Answer:
"""

        return prompt