from consts import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
                          InlineKeyboardButton, InlineKeyboardMarkup

button_hello1 = KeyboardButton("Hello1!")
button_hello2 = KeyboardButton("Hello2!")
button_hello3 = KeyboardButton("Hello3!")

first_kb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
first_kb.row(button_hello1, button_hello2, button_hello3)
first_kb.row(button_hello1)
first_kb.row(button_hello2, button_hello3)
first_kb.row(button_hello1, button_hello2, button_hello3, button_hello1, button_hello2, button_hello3)
first_kb.row(*([button_hello1] * 24))


btn1 = InlineKeyboardButton("Моя прелесть", callback_data=BUTTON1)
second_kb = InlineKeyboardMarkup()
second_kb.add(btn1)