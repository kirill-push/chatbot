import os

from model import BlenderChatbot
from telegram import Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    MessageHandler,
    Updater,
)

chatbot = BlenderChatbot()


def start(update: Update, context: CallbackContext) -> None:
    first_message = "Hello! I am your chatbot. Ask me anything!"
    update.message.reply_text(first_message)
    chatbot.add_message(content=first_message)


def get_response(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    response = chatbot.get_response(user_input)
    update.message.reply_text(response)


def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Help!")


def main() -> None:
    try:
        updater = Updater(str(os.environ.get("TELEGRAM_TOKEN")), use_context=True)
    except Exception:
        with open(".token", "r") as file:
            token = file.readline().strip("\n")
            updater = Updater(token, use_context=True)

    dp = updater.dispatcher  # type: ignore

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, get_response))

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
