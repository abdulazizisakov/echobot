from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update

from settings import TOKEN


def start(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text="Salom xush kelibsiz.",
    )


def help(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text="Qanday yordam berolaman.",
    )


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        handler=CommandHandler(command=["start", "boshlash"], callback=start)
    )
    dispatcher.add_handler(
        handler=CommandHandler(command=["help", "yordam"], callback=help)
    )

    updater.start_polling()
    updater.idle()


main()
