import handlers
from telegram.ext import Updater, CommandHandler
from config import TOKEN


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    # command handler
    dispatcher.add_handler(CommandHandler("start", handlers.start))
    dispatcher.add_handler(CommandHandler("keyboard", handlers.send_keyboard))
    dispatcher.add_handler(CommandHandler("inline_keyboard", handlers.send_inline_keyboard))

    # start bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
