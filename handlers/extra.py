from keyboards import client_kb
from aiogram import types, Dispatcher

from config import bot


# @dp.message_handler()



async def echo(message: types.Message):
    if message.text.startswith('!pin'):
        if not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
        return

    if message.text.lower() == 'dice':
        await bot.send_message(message.chat.id, f"Кидает бот")
        a = await bot.send_dice(message.chat.id, emoji='🎲')
        await bot.send_message(message.chat.id, f"Кидает игрок")
        b = await bot.send_dice(message.chat.id, emoji='🎲')
        if a.dice.value > b.dice.value:
            await bot.send_message(message.chat.id,
                                   f"У бота {a.dice.value} и у игрока {b.dice.value}\n"
                                   "Победитель бот")
            return
        elif a.dice.value < b.dice.value:
            await bot.send_message(message.chat.id,
                                   f"У бота {a.dice.value} и у игрока {b.dice.value}\n"
                                   "Победитель игрок")
            return
        else:
            await bot.send_message(message.chat.id,
                                   f"У бота {a.dice.value} и у игрока {b.dice.value}\n"
                                   "Ничья")
            return

    elif message.text == "🧆 Меню":
        await bot.send_message(message.chat.id, '🧆 Меню', reply_markup=client_kb.menu_markup)

    a = message.text
    try:
        b = 1
        a = int(a)
    except:
        pass
        b = 0
    if b == 1:
        await bot.send_message(message.chat.id, f"{a ** 2}")
    elif b == 0:
        await bot.send_message(message.chat.id, a)


def register_message_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
