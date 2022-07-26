import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="ok")


async def go_to_class():
    await bot.send_message(chat_id=chat_id, text="Пора учиться!")


async def go_to_work():
    photo = open("./media/2.jpg", 'rb')
    await bot.send_photo(chat_id=chat_id, photo=photo)


async def scheduler():
    aioschedule.every().monday.at("07:00").do(go_to_work)
    aioschedule.every().tuesday.at("18:00").do(go_to_class)
    aioschedule.every().friday.at("18:00").do(go_to_class)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(10)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: "напомни" in word.text)

