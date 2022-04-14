import logging
from loader import dp
from aiogram.types import Message, CallbackQuery
from keyboards.inline.productsKeyboard import categoryMenu, productMenu, booksMenu




@dp.message_handler(text_contains="Mahsulotlar")
async def select_category(message: Message):
    await message.answer(f"Mahsulot tanlang", reply_markup=categoryMenu)

@dp.callback_query_handler(text="reka")
async def buy_reka(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.delete()
    await call.message.answer("Reka Turin Tanlang", reply_markup=productMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="books")
async def buy_book(call: CallbackQuery):
    await call.message.answer("Tavarlar", reply_markup=booksMenu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancel")
async def cancel_buyin(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer()