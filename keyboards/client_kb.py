from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

style_1 = KeyboardButton("Первые блюда")
style_2 = KeyboardButton("Вторые блюда")
style_3 = KeyboardButton("Салаты")
style_4 = KeyboardButton("Закустки")
style_5 = KeyboardButton("Десерты")
style_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
style_markup.row(style_1, style_2)
style_markup.add(style_3, style_4, style_5)

cancel_button = KeyboardButton('CANCEL')
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True).add(cancel_button)
