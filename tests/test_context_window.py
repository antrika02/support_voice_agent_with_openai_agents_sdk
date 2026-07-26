from app.memory.conversation import Conversation

conversation = Conversation(max_messages=4)

for i in range(1, 8):
    conversation.add_user_message(
        f"Question {i}"
    )

for message in conversation.history():
    print(message.content)