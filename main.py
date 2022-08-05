from aiogram.utils import executor
from decouple import config

from config import dp, URL, bot
import logging
import asyncio
from handlers import client, callback, extra, admin, fsmAdminMenu, \
    notification, inline, fsmqrcode
from database.bot_db import sql_create


async def on_startup(_):
    await bot.set_webhook(URL)
    asyncio.create_task(notification.scheduler())
    sql_create()


async def on_shutdown(dp):
    await bot.delete_webhook()

client.register_handler_client(dp)
callback.register_handler_callback(dp)
admin.register_handler_admin(dp)
fsmAdminMenu.register_handlers_fsmmenu(dp)
fsmqrcode.register_handler_fsmqrcode(dp)
notification.register_handlers_notification(dp)
inline.register_inline_handler(dp)


extra.register_message_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path="",
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host='0.0.0.0',
        port=config("PORT", cast=int)
    )
