from aiogram import types
from loader import dp

@dp.inline_handler()
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="tavar001",
                title="Taxat Maxsultlari",
                input_message_content=types.InputTextMessageContent(
                    message_text="https://t.me/Aliksandrmax_bot"
                ),
                url="https://Timberg.uz"
            )
        ]
    )