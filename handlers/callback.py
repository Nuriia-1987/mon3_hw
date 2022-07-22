from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

from config import bot


# @dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('NEXT', callback_data='button_call_2')
    markup.add(button_call_2)

    question = "В честь какого животного назван самый распространненый язык программирования?"
    answer = [
        'Питон', 'Анаконда', 'Тигр'
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Легко",
        explanation_parse_mode=ParseMode.MARKDOWN,
        reply_markup=markup
    )


# @dp.callback_query_handler(lambda call: call.data == 'button_call_2')
async def quiz_3(call: types.CallbackQuery):
    question = "Отвечай!!!"
    answer = [
        '55', '32', '36', '16', '44'
    ]
    photo = open("media/1.jpg", 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Ошибочка",
        explanation_parse_mode=ParseMode.MARKDOWN
    )


def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(
        quiz_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(
        quiz_3, lambda call: call.data == 'button_call_2')
