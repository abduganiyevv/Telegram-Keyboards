import handlers
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from config import TOKEN


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    # command handler
    dispatcher.add_handler(CommandHandler("start", handlers.start))
    dispatcher.add_handler(CommandHandler("keyboard", handlers.send_keyboard))
    dispatcher.add_handler(CommandHandler("inline_keyboard", handlers.send_inline_keyboard))

    # message handler
    dispatcher.add_handler(MessageHandler(Filters.text("Mahsulotlar"), handlers.send_products))
    # dispatcher.add_handler(MessageHandler(Filters.text("Buyurtmalarim"), handlers.)) # add handler

    # callbackquery handler
    dispatcher.add_handler(CallbackQueryHandler(callback=handlers.handle_btn2, pattern='btn2'))

    # start bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
