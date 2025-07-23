from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Salom! Darslar kerak bo‘lsa /keyboard tugmasini bosing.")


def send_keyboard(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Darslar. O'zingizga kerakli bo'limni tanlang!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton('Frontend dasturlar'), KeyboardButton("Backend dasturlar"),KeyboardButton('No Code dasturlari')],
                [KeyboardButton('Dizaynerlik darslari'),KeyboardButton('Database'),KeyboardButton('Android')],
                [KeyboardButton('Mobilografiya darslari')],
                [KeyboardButton('SMM darslari'),KeyboardButton('Photoshop darslari')],
                [KeyboardButton('Kiberxavfsizlik darslari'),KeyboardButton('Videomontaj darslari')],
                [KeyboardButton('Telegram bot yaratish'),KeyboardButton('IQS')],
                [KeyboardButton("GitHub")],
            ],
            resize_keyboard=True,
        )
    )
frontend_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("CSS darslari"), KeyboardButton("SASS darslari"),KeyboardButton("SASS darslari"),KeyboardButton("Bootstrap darslari")],
        [KeyboardButton("JavaScript darslari"), KeyboardButton("React darslari")],
        [KeyboardButton("TypeScript darslari"),KeyboardButton("Bootstrap darslari")],
        [KeyboardButton("Go Back")],
    ],
    resize_keyboard=True
)


def handle_message(update, context):
    text = update.message.text

    if text == 'Frontend dasturlar':
        update.message.reply_text("Frontend bo‘limi ichidagi darslardan birini tanlang:", reply_markup=frontend_menu)

    elif text == 'HTML darslari':
        update.message.reply_text("HTML darslari:\nhttps://www.youtube.com/playlist?list=PLQWhzdFNj2CeAI0EFe0r5_vYaJUqMQxd-")

    elif text == 'CSS darslari':
        update.message.reply_text("CSS darslari:\nhttps://www.youtube.com/playlist?list=PLBoBu8c5jyTH790_UBbhtF0ZGnW8Alup5")

    elif text == 'SASS darslari':
        update.message.reply_text("SASS darslari:\nhttps://www.youtube.com/playlist?list=SASS_PLAYLIST_ID")

    elif text == 'Bootstrap darslari':
        update.message.reply_text("Bootstrap darslari:\nhttps://www.youtube.com/playlist?list=BOOTSTRAP_PLAYLIST_ID")

    elif text == 'JavaScript darslari':
        update.message.reply_text("JavaScript darslari:\nhttps://www.youtube.com/playlist?list=JS_PLAYLIST_ID")

    elif text == 'React darslari':
        update.message.reply_text("React darslari:\nhttps://www.youtube.com/playlist?list=REACT_PLAYLIST_ID")

    elif text == 'TypeScript darslari':
        update.message.reply_text("TypeScript darslari:\nhttps://www.youtube.com/playlist?list=TYPESCRIPT_PLAYLIST_ID")

    elif text == 'Orqaga':
        send_keyboard(update, context)


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


# def handle_btn2(update: Update, context: CallbackContext):
#     update.callback_query.answer("siz button 2 ni bosdingiz.")
