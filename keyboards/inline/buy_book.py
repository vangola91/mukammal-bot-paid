from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

book_keys = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Bizning Manzil', callback_data='mylocation'),
            InlineKeyboardButton(text="Kontent ulashish", callback_data="mycontact"),
        ],
    ]
)