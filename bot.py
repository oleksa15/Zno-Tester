from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.storage import FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import aiogram.utils.markdown as md

from config import token

import question
import answers
import buttons

bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


class Test(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()
    Q6 = State()
    Q7 = State()
    Q8 = State()
    Q9 = State()
    Q10 = State()

@dp.message_handler(commands=['start'], state=None)
async def procces_command_start(message: types.Message):
    await bot.send_message(message.chat.id, 'Для початку тесту напшіть /test')

@dp.message_handler(commands=['test'], state=None)
async def enter_test(message: types.Message):
    await message.answer(f'Ви почали тест.\n\
                {question.first}', reply_markup=buttons.first)

    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Q1'] = message.text

    await message.answer(f"Запитання №2.\n\
                {question.second}", reply_markup=buttons.second)

    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Q2'] = message.text

    await message.answer(f"Запитання №3.\n\
                {question.third}", reply_markup=buttons.third)

    await Test.next()


@dp.message_handler(state=Test.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Q3'] = message.text

    await message.answer(f'Запитання №4\n\
            {question.firth}', reply_markup=buttons.firth)

    await Test.next()


@dp.message_handler(state=Test.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Q4'] = message.text

    await message.answer(f'Запитання №5\n\
        {question.fifth}', reply_markup=buttons.fifth)

    await Test.next()


@dp.message_handler(state=Test.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Q5'] = message.text

    await message.answer(f'Запитання №6\n\
        {question.sixth}', reply_markup=buttons.sixth)
    
    await Test.next()

@dp.message_handler(state=Test.Q6)
async def answer_q6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Q6'] = message.text
    
    await message.answer(f'Запитання №7\n\
        {question.seventh}', reply_markup=buttons.seventh)
    
    await Test.next()

@dp.message_handler(state=Test.Q7)
async def answer_q7(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Q7'] = message.text
    
    await message.answer(f'Запитання №8\n\
        {question.eighth}', reply_markup=buttons.eighth)
    
    await Test.next()

@dp.message_handler(state=Test.Q8)
async def answer_q8(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Q8'] = message.text
    
    await message.answer(f'Запитання №9\n\
        {question.ninth}', reply_markup=buttons.ninth)
    
    await Test.next()

@dp.message_handler(state=Test.Q9)
async def answer_q9(message: types.message, state: FSMContext):
    async with state.proxy() as data:
        data['Q9'] = message.text
    
    await message.answer(f'Запитання №10\n\
        {question.tenth}', reply_markup=buttons.tenth)

    await Test.next()

@dp.message_handler(state=Test.Q10)
async def answer_q10(message: types.message, state: FSMContext):
    async with state.proxy() as data:
        data['Q10'] = message.text
        markup = types.ReplyKeyboardRemove()
    
    note = 0
    if md.bold(data['Q1']) == answers.first:
        note =+ 1
    
    elif md.bold(data['Q2']) == answers.second:
        note =+ 1
    
    elif md.bold(data['Q3']) == answers.third:
        note =+ 1
    
    elif md.bold(data['Q4']) == answers.firth:
        note =+ 1
    
    elif md.bold(data['Q5']) == answers.fifth:
        note =+ 1
    
    elif md.bold(data['Q6']) == answers.sixth:
        note =+ 1
    
    elif md.bold(data['Q7']) == answers.seventh:
        note =+ 1
    
    elif md.bold(data['Q8']) == answers.eighth:
        note =+ 1
    
    elif md.bold(data['Q9']) == answers.ninth:
        note =+ 1
    
    elif md.bold(data['Q10']) == answers.tenth:
        note =+ 1

    await bot.send_message(message.chat.id, f'Оцінка по 12 бальній = {note}\nОцінка по 200 бальній = {note*20}')
    await state.finish()
    
if __name__ == '__main__':
    executor.start_polling(dp)
