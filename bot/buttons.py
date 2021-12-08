# Buttons

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


first_answer = KeyboardButton('A)')
second_answer = KeyboardButton('Б)')
third_answer = KeyboardButton('В)')
fourh_answer = KeyboardButton('Г)')

buttons = ReplyKeyboardMarkup(resize_keyboard=True).add(first_answer, second_answer, third_answer, fourh_answer)
