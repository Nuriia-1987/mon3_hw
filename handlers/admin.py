from random import sample
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from config import bot, ADMIN


async def games(message: types.Message):
    emo = {'⚽', '🎲', '🎳', '🎰', '🎯', '🏈'}
    if message.text.lower() == 'game':
        if message.from_user.id not in ADMIN:
            await message.answer("Ты не админ этой группы!")
            return
        else:
            await bot.send_dice(message.chat.id, emoji=sample(emo, 1))
            return


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(games, commands=['game'])
    dp.register_message_handler(games, Text(equals='game', ignore_case=True), state='*')
