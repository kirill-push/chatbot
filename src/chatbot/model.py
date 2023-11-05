from typing import Optional

from transformers import Conversation, pipeline


class BlenderChatbot:
    def __init__(self, first_input: Optional[str] = None) -> None:
        self.chatbot = pipeline(
            "conversational", model="facebook/blenderbot-400M-distill"
        )
        self.restart_conversation(first_input)

    def add_message(self, role: str = "assistant", content: str = "") -> None:
        self.conversation.add_message({"role": role, "content": content})

    def restart_conversation(self, first_input: Optional[str] = None) -> None:
        self.conversation = Conversation(first_input)

    def get_response(self, user_input: str) -> str:
        self.conversation.add_user_input(user_input)
        self.conversation = self.chatbot(self.conversation)
        response = self.conversation.generated_responses[-1]
        return response
