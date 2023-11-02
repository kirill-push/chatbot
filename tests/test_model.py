import pytest
from model import BlenderChatbot


@pytest.fixture
def chatbot() -> BlenderChatbot:
    return BlenderChatbot()


def test_initialization(chatbot: BlenderChatbot) -> None:
    assert chatbot.chatbot is not None
    assert chatbot.conversation is not None


def test_get_response(chatbot: BlenderChatbot) -> None:
    user_input = "Hello"
    response = chatbot.get_response(user_input)

    assert isinstance(response, str)
    assert response != ""

    new_user_input = "How are you?"
    new_response = chatbot.get_response(new_user_input)

    assert new_response != ""


def test_add_message(chatbot: BlenderChatbot) -> None:
    new_bot_message = "Hi!"
    old_messages = chatbot.conversation.messages.copy()
    chatbot.add_message(content=new_bot_message)
    assert chatbot.conversation.messages != old_messages

    user_input = "Hello!"
    assert chatbot.get_response(user_input) != ""
