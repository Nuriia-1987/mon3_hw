
from aiogram import Bot, Dispatcher
from decouple import config

from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN = [1746047370, ]
CHANNEL_ID = "@test_bot_N"
URL = "https://nuri777bot.herokuapp.com/"
PORT = config('PORT')
