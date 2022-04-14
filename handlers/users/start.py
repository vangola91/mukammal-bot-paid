import logging
from data.config import CHANNELS
from aiogram import types
from keyboards.inline.subscription import check_button

from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.startMenuKeyboard import menuStart
from loader import dp, bot
from utils.misc import subscription

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




@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    #logging.info(message)
    logging.info(f"{message.from_user.id=}")
    logging.info(f"{message.from_user.full_name=}")
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menuStart)

