# import datetime
# from unittest.mock import MagicMock, patch

# import pytest
# from telegram import Chat, Message, Update, User, Bot
# from telegram.ext import CallbackContext
# from telegram_bot import get_response, help, start


# @pytest.fixture
# def fake_update() -> MagicMock:
#     user = User(id=2, first_name="testuser", is_bot=False)
#     chat = Chat(id=3, type="private")
#     message = Message(
#         message_id=1,
#         date=datetime.datetime.now(),
#         chat=chat,
#         text="Test",
#         from_user=user,
#         bot=MagicMock(spec=Bot)
#     )

#     update = MagicMock(spec=Update)
#     update.message = message
#     update.update_id = 123
#     update._id_attrs = (update.update_id,)

#     # update.configure_mock(update_id=123, message=message)

#     return update


# @pytest.fixture
# def fake_context() -> MagicMock:
#     context = MagicMock(spec=CallbackContext)
#     return context


# def test_start(fake_update: MagicMock, fake_context: MagicMock) -> None:
#     with patch("telegram_bot.chatbot") as mock_chatbot:
#         start(fake_update, fake_context)
#         fake_update.message.reply_text.assert_called_once_with(
#             "Hello! I am your chatbot. Ask me anything!"
#         )
#         mock_chatbot.add_message.assert_called_once_with(
#             content="Hello! I am your chatbot. Ask me anything!"
#         )


# def test_get_response(fake_update: MagicMock, fake_context: MagicMock) -> None:
#     with patch("telegram_bot.chatbot") as mock_chatbot:
#         mock_chatbot.get_response.return_value = "This is a response"
#         get_response(fake_update, fake_context)
#         mock_chatbot.get_response.assert_called_once_with(fake_update.message.text)
#         fake_update.message.reply_text.assert_called_once_with("This is a response")


# def test_help(fake_update: MagicMock, fake_context: MagicMock) -> None:
#     help(fake_update, fake_context)
#     fake_update.message.reply_text.assert_called_once_with("Help!")

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
