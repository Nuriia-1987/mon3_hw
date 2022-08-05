from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

style_1 = KeyboardButton("Первые блюда")
style_2 = KeyboardButton("Вторые блюда")
style_3 = KeyboardButton("Салаты")
style_4 = KeyboardButton("Закустки")
style_5 = KeyboardButton("Десерты")
style_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
style_markup.row(style_1, style_2)
style_markup.add(style_3, style_4, style_5)

cancel_button = KeyboardButton('cancel')
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True).add(cancel_button)

cancel_qr_button = KeyboardButton("CANCEL QR")
cancel_qr_markup = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(cancel_qr_button)

# url_channel_button = InlineKeyboardButton("Подписаться", url="https://t.me/test_bot_N")
# done_button = InlineKeyboardButton("Подписался", callback_data='subchanneldone')
# check_sub_menu = InlineKeyboardMarkup(row_width=2).add(url_channel_button, done_button)

menu_button = KeyboardButton("/menu")
random_dish = KeyboardButton("/random_dish")
show_menu = KeyboardButton("/show_menu")
delete_dish = KeyboardButton("/del_dish")

menu_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(menu_button, random_dish, show_menu, delete_dish)

btnMenu = KeyboardButton("🧆 Меню")

start_button = KeyboardButton("/start")
mem_button = KeyboardButton("/mem")
help_button = KeyboardButton("/help")
quiz_button = KeyboardButton("/quiz")
game_button = KeyboardButton("game")
dice_button = KeyboardButton("/dice")
pin_button = KeyboardButton("!pin")
training_button = KeyboardButton("напомни")


start_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(start_button, pin_button, help_button,
                                                             quiz_button, game_button, dice_button,
                                                             btnMenu, training_button)



