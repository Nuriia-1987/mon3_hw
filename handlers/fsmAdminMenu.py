from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import client_kb
from config import bot, ADMIN


class FSMAdmin(StatesGroup):
    photo = State()
    style = State()
    name = State()
    description = State()
    weight = State()
    price = State()


async def fsm_start(message: types.Message):
    if message.from_user.id in ADMIN:
        await FSMAdmin.photo.set()
        await message.answer(f"Приведствую Вас {message.from_user.full_name} "
                             f"скинь фото блюда ...", reply_markup=client_kb.cancel_markup)
    else:
        await message.reply("Вы не админ!")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Тип блюда", reply_markup=client_kb.style_markup)


async def load_style(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["style"] = message.text
    await FSMAdmin.next()
    await message.answer("Полное название блюда", reply_markup=client_kb.cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Полное описание блюда?", reply_markup=client_kb.cancel_markup)


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer("Вес блюда?", reply_markup=client_kb.cancel_markup)


async def load_weight(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['weight'] = f'{int(message.text)} грамм'
        await FSMAdmin.next()
        await message.answer("Цена блюда?", reply_markup=client_kb.cancel_markup)
    except:
        await message.answer("Пишите цифрами!")


async def load_price(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['price'] = f'{int(message.text)} сом'
    except:
        await message.answer("Пишите цифрами!")
    await bot.send_photo(message.chat.id, data['photo'],
                         caption=f"Type: {data['style']}\n"
                                 f"Name: {data['name']}\n"
                                 f"Description: {data['description']}\n"
                                 f"Weight: {data['weight']}\n"
                                 f"Price: {data['price']}")

    await state.finish()
    await message.answer("Все готово!")


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer("Регистрация блюда отмененна!")


def register_handlers_fsmmenu(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state='*', commands="cancel")
    dp.register_message_handler(cancel_registration,
                                Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['menu'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(load_style, state=FSMAdmin.style)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_weight, state=FSMAdmin.weight)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
