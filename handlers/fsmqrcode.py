from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import bot
import pyqrcode
from keyboards.client_kb import cancel_qr_markup


class FSMAdmin(StatesGroup):
    get_text = State()


async def fsm_qr_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.get_text.set()
        await bot.send_message(
            message.chat.id,
            f"Привет {message.from_user.full_name}, "
            f"отправь мне любой текст или ссылку\n"
            f"Для выхода из режима нажми на кнопку /cancel_qr",
            reply_markup=cancel_qr_markup
        )
    else:
        await message.answer("Пиши в личку!")


async def do_qr(message: types.Message, state: FSMContext):
    qr_code = pyqrcode.create(message.text)
    qr_code.png("media/code.png", scale=6)
    photo = open("media/code.png", "rb")
    await bot.send_photo(message.from_user.id, photo,
                         caption="Ваш QR код говов, вы можете присласть еще!\n"
                                 "Для выхода из режима нажми на кнопку /cancel_qr")


async def cancel_qr(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.reply("Вы вышли из режима QR кода!")


def register_handler_fsmqrcode(dp: Dispatcher):
    dp.register_message_handler(cancel_qr, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_qr,
                                Text(equals='cancel qr', ignore_case=True), state='*')
    dp.register_message_handler(fsm_qr_start, commands=['qr'])
    dp.register_message_handler(do_qr, state=FSMAdmin.get_text)
