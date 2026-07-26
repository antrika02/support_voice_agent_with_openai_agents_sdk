from app.prompt_builder import PromptBuilder
from app.memory.conversation import Conversation


conversation = Conversation()

conversation.add_user_message(
    "What is Python?"
)

conversation.add_assistant_message(
    "Python is a programming language."
)

builder = PromptBuilder()


class DummyResult:
    def __init__(self, text):
        self.payload = {
            "content": text
        }


results = [
    DummyResult(
        "Python supports inheritance through classes."
    )
]

prompt = builder.build(
    question="What about inheritance?",
    results=results,
    history=conversation.history()
)

print(prompt)