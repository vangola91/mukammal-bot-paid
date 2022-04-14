from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import tavar_callback, book_callback

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Река", callback_data="reka"),
            InlineKeyboardButton(text="Вагонка", callback_data="vagonka"),
            InlineKeyboardButton(text="Гули Рекалар", callback_data="guli"),
            InlineKeyboardButton(text="kitoblar", callback_data="bookss"),

        ],
    ],
)
productMenu = InlineKeyboardMarkup(row_width=1)

tavriko = InlineKeyboardButton(text="Таврико", callback_data=tavar_callback.new(item_name="tavriko"))
productMenu.insert(tavriko)

brus = InlineKeyboardButton(text="Брус", callback_data=tavar_callback.new(item_name="brus"))
productMenu.insert(brus)


back_button = InlineKeyboardButton(text="Ortga", callback_data="cancel")
productMenu.insert(back_button)

bookss = {
    "Таврико. Mamayov  ": "tavriko",
    "Брус.": "brus",
    "guli rekalar": "gul",

}
booksMenu = InlineKeyboardMarkup(row_width=1)
for key, value in bookss.items():
    booksMenu.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))
booksMenu.insert((back_button))

