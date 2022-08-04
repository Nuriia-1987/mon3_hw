from aiogram.utils import executor
from config import dp
import logging
import asyncio
from handlers import client, callback, extra, admin, fsmAdminMenu, \
    notification, inline
from database.bot_db import sql_create


async def on_startup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()

client.register_handler_client(dp)
callback.register_handler_callback(dp)
admin.register_handler_admin(dp)
fsmAdminMenu.register_handlers_fsmmenu(dp)
notification.register_handlers_notification(dp)
inline.register_inline_handler(dp)


extra.register_message_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
