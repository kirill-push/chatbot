import pytest

from chatbot.model import DialoGPTChatbot


@pytest.fixture
def chatbot():
    return DialoGPTChatbot()


def test_initialization(chatbot):
    assert chatbot.tokenizer is not None
    assert chatbot.model is not None
    assert chatbot.chat_history_ids is None


def test_get_response(chatbot):
    user_input = "Hello"
    response = chatbot.get_response(user_input)

    assert isinstance(response, str)
    assert response != ""
