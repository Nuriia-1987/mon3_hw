from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

from config import bot, CHANNEL_ID
from handlers.services import check_sub_channel
from keyboards import client_kb


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


async def subchanneldone(call: types.CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=call.message.from_user.id)):
        await bot.send_message(call.message.chat.id,
                               f"Приветствую Вас! {call.message.from_user.full_name}",
                               reply_markup=client_kb.start_markup)
    else:
        await bot.send_message(call.message.from_user.id,
                               f"Чтобы пользоваться ботомб подпишись на канал",
                               reply_markup=client_kb.chack_sub_menu)


def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(
        quiz_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(
        quiz_3, lambda call: call.data == 'button_call_2')
