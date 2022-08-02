from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

from config import bot
from keyboards import client_kb
from database.bot_db import dql_command_random
from panser import food


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Приветствую Вас! {message.from_user.full_name}")


# @dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"{message.from_user.full_name} Помоги себе сам!!!!")


# @dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    photo2 = open('media/tn2jcjcglxxx.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo2)


# @dp.message_handler(commands=['quiz'])
async def quiz_handler(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    markup.add(button_call_1)

    question = "True к какому типу данных относяться?"
    answer = [
        'Int', 'Str', 'Bool', 'Нет такого типа'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Будь внимателен",
        explanation_parse_mode=ParseMode.MARKDOWN,
        reply_markup=markup
    )


async def show_random_user(message: types.Message):
    await dql_command_random(message)


async def parser_pizza(message: types.Message):
    data = food.parser()[:10]
    for item in data:
        await bot.send_message(
            message.chat.id,
            f'{item["title"]}\n'
            f'{item["disc"]}\n'
            f'{item["price"]}\n'
            f'{item["photo"]}'
        )


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(help_handler, commands=['help'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(quiz_handler, commands=['quiz'])
    dp.register_message_handler(show_random_user, commands=['random'])
    dp.register_message_handler(parser_pizza, commands=['pizza'])
