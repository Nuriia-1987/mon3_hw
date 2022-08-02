import hashlib
from aiogram import types, Dispatcher


async def inline_wikiped_handker(query: types.InlineQuery):
    text = query.query or "echo"
    link = f"https://ru.wikipedia.org/wiki/{text}"
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title="Wikipedia: ",
        url=link,
        input_message_content=types.InputMessageContent(
            messge_text=link
        )
    )]
    await query.answer(articles, cache_time=60, is_personal=True)


def register_handler_inline(dp: Dispatcher):
    dp.register_inline_handler(inline_wikiped_handker)