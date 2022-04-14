from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hstrikethrough, hlink
from loader import dp


@dp.message_handler(commands="info_html")
async def bot_help(message: types.Message):
    text = f"Asalom alaykum,{message.from_user.full_name}!\n"
    text += "Nima Yordam Beraolaman"

    await message.answer(text)

