
from aiogram import Bot, Dispatcher, executor, types

from config import token

import buttons

bot = Bot(
    token
)
dp = Dispatcher(
    bot=bot
)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=buttons.buttons)

if __name__ == '__main__':
   executor.start_polling(dp)