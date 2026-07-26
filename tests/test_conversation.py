from app.memory.conversation import Conversation

conversation = Conversation()

conversation.add_user_message(
    "What is Python?"
)

conversation.add_assistant_message(
    "Python is a programming language."
)

conversation.add_user_message(
    "What about inheritance?"
)

for message in conversation.history():

    print(message.role)

    print(message.content)

    print("-" * 40)