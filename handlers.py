from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Salom! Darslar kerak bo‘lsa /keyboard tugmasini bosing.")


def send_keyboard(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Keyboard.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton('Frontend dasturlar'), KeyboardButton("Backend dasturlar"),KeyboardButton('No Code dasturlari')],
                [KeyboardButton('Dizaynerlik darslari'),KeyboardButton('Database'),KeyboardButton('Android')],
                [KeyboardButton("Bog‘lanish")],
            ],
            resize_keyboard=True,
        )
    )


def handle_message(update, context):
    text = update.message.text

    if text == 'Frontend dasturlar':
        update.message.reply_text(
            "---Frontend darslari---\n" \
            "CSS, SASS, JavaScript, React, HTML darslari\n"
            "👇👇👇\n"
            " https://www.youtube.com/playlist?list=PLBoBu8c5jyTH790_UBbhtF0ZGnW8Alup5",
        )
    elif text == 'Backend dasturlar':
        update.message.reply_text(
            "---Backend darslari---\n"
            "C++, PYTHON darslari\n"
            "👇👇👇\n"
            "https://www.youtube.com/playlist?list=PLwsopmzfbOn_1XLqRYV7gu8ozcYvPEqmd"
        )
    elif text == 'No Code dasturlari':
        update.message.reply_text(
            "---No Code darslari---\n"
            "Telegram bot yaratish, Sayt yaratish darslari\n"
            "👇👇👇\n"
            "https://www.youtube.com/playlist?list=PLtJ-ufoDnA2DQIO-UBOIWiQffp7DC9xn5"

        )
    elif text == 'Dizaynerlik darslari':
        update.message.reply_text(
            "---Dizayn darslari---\n"
            "Figma, Canva Grafik dizayn darslari\n"
            "👇👇👇\n"
            "https://www.youtube.com/playlist?list=PLQWhzdFNj2CeAI0EFe0r5_vYaJUqMQxd-"
        )
    elif text == 'Database':
        update.message.reply_text(
            "---Database darslari---\n"
            "PostgreSQL, MySQL, MongoDB darslari\n"
            "👇👇👇\n"
            "https://www.youtube.com/playlist?list=PLcVkxa4hDY3HMSLeg6QOLftJUhLX2JJPe"

        )
    elif text == 'Android':
        update.message.reply_text(
            "---Android darslari---\n"
            "Kotlin, Java va Android darslari\n"
            "👇👇👇\n"
            "https://www.youtube.com/playlist?list=PL2MlJHnfSUYrkWMLoq6-rs6C6vkXuAZSj"
        )
    elif text == 'Bog‘lanish':
        update.message.reply_text("Admin bilan bog‘lanish:\n" \
        "" \
        "https://t.me/firdavsbek_abduganiyev")
    else:
        update.message.reply_text("Iltimos, menyudan tanlang.")



# def send_inline_keyboard(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         text="Inline Keyboard.",
#         reply_markup=InlineKeyboardMarkup(
#             inline_keyboard=[
#                 [InlineKeyboardButton('button 1', url="https://kun.uz/"), InlineKeyboardButton('button 2', callback_data='btn2')]
#             ]
#         )
#     )


def send_products(update: Update, context: CallbackContext):
    update.message.reply_text("Mahsulotlar royxati.")


def handle_btn2(update: Update, context: CallbackContext):
    update.callback_query.answer("siz button 2 ni bosdingiz.")
