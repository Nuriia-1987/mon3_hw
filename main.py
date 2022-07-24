from aiogram.utils import executor
from config import dp
import logging

from handlers import client, callback, extra, admin, fsmAdminMenu
from database.bot_db import sql_create


async def on_startup(_):
    sql_create()

client.register_handler_client(dp)
callback.register_handler_callback(dp)
admin.register_handler_admin(dp)
fsmAdminMenu.register_handlers_fsmmenu(dp)


extra.register_message_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
