from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

#Перше
answer1_A = KeyboardButton('А) Олесь Тихий')
answer1_B = KeyboardButton('Б) Віктор Грім')
answer1_C = KeyboardButton('В) Тарас Чупринка')
answer1_D = KeyboardButton('Г) Василь Вишиваний')

first = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
first.add(answer1_A, answer1_B, answer1_C, answer1_D)

#Друге
answer2_A = KeyboardButton('А) Рада Міністрів')
answer2_B = KeyboardButton('Б) Штаб Київського військового округу')
answer2_C = KeyboardButton('В) Генеральний Секретаріат')
answer2_D = KeyboardButton('Г) Рада Народних Комісарів')

second = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
second.add(answer2_A, answer2_B, answer2_C, answer2_D)

answer3_A = KeyboardButton('А) Грамоти до всього українського народу гетьмана П. Скоропадського.')
answer3_B = KeyboardButton('Б) Конституції Української Народної Республіки.')
answer3_C = KeyboardButton('В) Акта злуки між УНР й ЗУНР.')
answer3_D = KeyboardButton('Г) Третього Універсалу УЦР.')

third = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
third.add(answer3_A, answer3_B, answer3_C, answer3_D)

# Четверте 
answer4_A = KeyboardButton('А) 1914 р.')
answer4_B = KeyboardButton('Б) 1917 р.')
answer4_C = KeyboardButton('В) 1919 р.')
answer4_D = KeyboardButton('Г) 1921 р.')

firth = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
firth.add(answer4_A, answer4_B, answer4_C, answer4_D)

# П'яте
answer5_A = KeyboardButton('А) «воєнного комунізму»."')
answer5_B = KeyboardButton('Б) «культурної революції».')
answer5_C = KeyboardButton('В) «пацифікації».')
answer5_D = KeyboardButton('Г) «осадництва».')

fifth = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
fifth.add(answer4_A, answer4_B, answer4_C, answer4_D)

#Шосте
answer6_A = KeyboardButton('А) скасування плати за житло й комунальні послуги')
answer6_B = KeyboardButton('Б) здійснення насильницької суцільної колективізації')
answer6_C = KeyboardButton('В) уведення карткової системи розподілу продуктів')
answer6_D = KeyboardButton('Г) надання селянам права на продаж власної сільгосппродукції')

sixth = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
sixth.add(answer6_A, answer6_B, answer6_C, answer6_D)

#Сьоме
answer7_A = KeyboardButton('А) індустріалізацію')
answer7_B = KeyboardButton('Б) неп')
answer7_C = KeyboardButton('В) коренізацію')
answer7_D = KeyboardButton('Г) колективізацію')

seventh = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
seventh.add(answer7_A, answer7_B, answer7_C, answer7_D)

#Восьме
answer8_A = KeyboardButton('А) 1921 р.')
answer8_B = KeyboardButton('Б) 1925 р.')
answer8_C = KeyboardButton('В) 1934 р.')
answer8_D = KeyboardButton('Г) 1937 р.')

eighth = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
eighth.add(answer8_A, answer8_B, answer8_C, answer8_D)

#Дев'яте
answer9_A = KeyboardButton('А) Польщі')
answer9_B = KeyboardButton('Б) Чехословаччини')
answer9_C = KeyboardButton('В) Румунії')
answer9_D = KeyboardButton('Г) Української ССР')

ninth = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
ninth.add(answer9_A, answer9_B, answer9_C, answer9_D)

#Десяте
answer10_A = KeyboardButton('А) сіру зону')
answer10_B = KeyboardButton('Б) випалену землю')
answer10_C = KeyboardButton('В) життєвий простір')
answer10_D = KeyboardButton('Г) санітарний кордон')

tenth = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
tenth.add(answer10_A, answer10_B, answer10_C, answer10_D)


# Инлайн кнопка
 
test_btn = InlineKeyboardButton('Почати Тест', callback_data='/test')
test_kb = InlineKeyboardMarkup().add(test_btn)
