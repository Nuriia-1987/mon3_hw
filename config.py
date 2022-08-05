from aiogram import Bot, Dispatcher
import decouple

from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = decouple.config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN = [1746047370, ]
CHANNEL_ID = "@test19ch"
URL = "https://nuri777bot.herokuapp.com/"
