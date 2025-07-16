from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    update.message.reply_text("salom, \n\n/keyboard\n/inline_keyboard")


def send_keyboard(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Keyboard.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton('Mahsulotlar'), KeyboardButton("Buyurtmalarim")],
                [KeyboardButton('Contact', request_contact=True), KeyboardButton("Location", request_location=True)],
            ],
            resize_keyboard=True,
        )
    )


def send_inline_keyboard(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Inline Keyboard.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton('button 1', url="https://kun.uz/"), InlineKeyboardButton('button 2', callback_data='btn2')]
            ]
        )
    )


def send_products(update: Update, context: CallbackContext):
    update.message.reply_text("Mahsulotlar royxati.")


def handle_btn2(update: Update, context: CallbackContext):
    update.callback_query.answer("siz button 2 ni bosdingiz.")
