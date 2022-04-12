from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛒Mahsulotlar"),
            KeyboardButton(text="Qollanma"),
        ],
    ],
    resize_keyboard=True
)