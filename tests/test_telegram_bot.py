from unittest.mock import MagicMock, patch

import pytest
from pytest_mock import MockerFixture
from telegram import Chat, Message, Update, User
from telegram_bot import get_response, help, start


@pytest.fixture
def mock_update(mocker: MockerFixture) -> MagicMock:
    update = MagicMock(spec=Update)
    update.message = MagicMock(spec=Message)
    update.message.text = "test"
    update.message.chat = MagicMock(spec=Chat)
    update.message.chat.id = 123456
    update.message.from_user = MagicMock(spec=User)
    update.message.from_user.id = 11111
    update.effective_chat = update.message.chat
    update.message.reply_text = MagicMock()
    return update


@pytest.fixture
def mock_context(mocker: MockerFixture) -> MagicMock:
    context = MagicMock()
    return context


def test_start(mock_update: MagicMock, mock_context: MagicMock) -> None:
    start(mock_update, mock_context)
    mock_update.message.reply_text.assert_called_with(
        "Hello! I am your chatbot. Ask me anything!"
    )


def test_help(mock_update: MagicMock, mock_context: MagicMock) -> None:
    help(mock_update, mock_context)
    mock_update.message.reply_text.assert_called_with("Help!")


def test_get_response(mock_update: MagicMock, mock_context: MagicMock) -> None:
    with patch("telegram_bot.chatbot.get_response", return_value="response"):
        mock_update.message.text = "test"
        mock_context.bot = MagicMock()
        get_response(mock_update, mock_context)
        expected_response = "response"
        mock_update.message.reply_text.assert_called_with(expected_response)
