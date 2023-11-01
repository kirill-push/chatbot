import pytest

from chatbot.model import DialoGPTChatbot


@pytest.fixture
def chatbot() -> DialoGPTChatbot:
    return DialoGPTChatbot()


def test_initialization(chatbot: DialoGPTChatbot) -> None:
    assert chatbot.tokenizer is not None
    assert chatbot.model is not None
    assert chatbot.chat_history_ids.nelement() == 0


def test_get_response(chatbot: DialoGPTChatbot) -> None:
    user_input = "Hello"
    response = chatbot.get_response(user_input)

    assert isinstance(response, str)
    assert response != ""

    new_user_input = "How are you?"
    new_response = chatbot.get_response(new_user_input)

    assert new_response != ""
