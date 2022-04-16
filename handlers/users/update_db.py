from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, db


@dp.message_handler(Command("email"))
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Email Manzilingizni Yuboring")
    await state.set_state("email")


@dp.message_handler(state="email")
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    db.update_users_email(email=email, id=message.from_user.id)
    user = db.select_users(id=message.from_user.id)
    await message.answer(f"Baza Yangilandi: {user}")
    await state.finish()
