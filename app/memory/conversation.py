from dataclasses import dataclass


@dataclass
class Message:
    role: str
    content: str


class Conversation:
    """
    Stores conversation history.
    """

    def __init__(self, max_messages: int = 10):
        self.messages = []
        self.max_messages = max_messages


    def _trim_history(self):
        """
        Keep only the latest messages.
        """

        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def add_user_message(self, message: str):
        self.messages.append(
            Message(
                role="user",
                content=message
            )
        )

        self._trim_history()

    def add_assistant_message(self, message: str):
        self.messages.append(
            Message(
                role="assistant",
                content=message
            )
        )

        self._trim_history()

    def history(self):
        return self.messages

    def clear(self):
        self.messages.clear()