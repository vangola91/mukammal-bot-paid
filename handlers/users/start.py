import logging
#import sqlite3
import asyncpg.exceptions

from data.config import ADMINS
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.startMenuKeyboard import menuStart
from loader import dp, db, bot
#from utils.misc import subscription

#kanlaga obuna tekshirish
# @dp.message_handler(commands=["start"])
# async def show_channels(message: types.Message):
#     channels_format = str()
#     for channel in CHANNELS:
#         chat = await bot.get_chat(channel)
#         invite_link = await chat.export_invite_link()
#
#         channels_format += f"<a href='{invite_link}'>{chat.title}</a>\n"
#
#     await message.answer(f"Botdan foydalanish uchun, quydagi kanallarga obuna bo'ling: \n"
#                          f"{channels_format}",
#                          reply_markup=check_button,
#                          disable_web_page_preview=True)
#
#
# @dp.callback_query_handler(text="check_subs")
# async def checker(call: types.CallbackQuery):
#     await call.answer()
#     result = str()
#     for channel in CHANNELS:
#         status = await subscription.check(user_id=call.from_user.id,
#                                             channel=channel)
#         channel =await bot.get_chat(channel)
#         if status:
#             result += f"<b>{channel.title}</b> kanaliga obuna bolgansiz!\n\n"
#         else:
#             invite_link = await channel.export_invite_link()
#             result += (f"<b>{channel.title}</b> kanalinga obuna bo'lmagansiz. "
#                         f"<a href='{invite_link}'>Obuna bo'ling </a>\n\n")
#     await call.message.answer(result, disable_web_page_preview=True)



#Sqlift bazasiz bialn ishlash
# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     name = message.from_user.full_name
#     # Userni bazaga qoshamiza
#     try:
#         db.add_user(id=message.from_user.id,
#                     name=name)
#     except sqlite3.IntegrityError as err:
#         await bot.send_message(chat_id=ADMINS[0], text=err)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    try:
        user =db.add_user(telegram_id==message.from_user.id,
                          full_name=message.from_user.full_name,
                          username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await dp.select_user()
        await bot.send_message(chat_id=ADMINS[0], text=err)



    await message.answer(f"Asalom Alekum \n Xush kelibsiz, {message.from_user.full_name}!", reply_markup=menuStart)
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qoshildi. \nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)

