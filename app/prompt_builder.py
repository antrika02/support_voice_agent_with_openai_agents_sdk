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

Answer the user's question using ONLY the documentation provided below.

If the documentation contains enough information to answer the question,
write a concise and accurate answer in your own words.

Do not use outside knowledge.

Only respond with:

"I couldn't find that information in the documentation."

if the documentation is clearly unrelated to the user's question.

Documentation
-------------
{documentation}
-------------

Question:
{question}

Answer:
"""

        return prompt