import hashlib
from pprint import pprint

from aiogram import types, Dispatcher
from youtube_search import YoutubeSearch as YT


def finder(text):
    result = YT(text, max_results=18).to_dict()
    return result


# pprint(finder("slivki"))


async def inline_youtube_handlers(query: types.InlineQuery):
    text = query.query or "echo"
    links = finder(text)
    articles = [types.InlineQueryResultArticle(
        id=hashlib.md5(f"{link['id']}".encode()).hexdigest(),
        title=f"{link['title']}",
        url=f"http://www.youtube.com/match?v={link['id']}",
        thumb_url=f"{link['thumbnails'][0]}",
        input_message_content=types.InputMessageContent(
            message_text=f"http://www.youtube.com/match?v={link['id']}"
        )
    ) for link in links]
    await query.answer(articles, cache_time=60, is_personal=True)


async def inline_wiki_handler(query: types.InlineQuery):
    text = query.query or "echo"
    link = f"https://ru.wikipedia.org/wiki/{text}"
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title="WIKI: ",
        url=link,
        input_message_content=types.InputMessageContent(
            messge_text=link
        )
    )]
    await query.answer(articles, cache_time=60, is_personal=True)


def register_inline_handler(dp: Dispatcher):
    # dp.register_inline_handler(inline_youtube_handlers)
    dp.register_inline_handler(inline_wiki_handler)
