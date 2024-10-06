from aiogram import Bot, Dispatcher, types, executor
#pip install aiogram==2.23.1
#pip install --force-reinstall -v "aiogram==2.23.1"
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv 
import os

load_dotenv()
Token = os.getenv('TOKEN')
bot = Bot(token=Token)
dp = Dispatcher(bot)

@dp.callback_query_handler(lambda c: c.data == 'yes')
async def press_button(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Вы нажали Да')

@dp.callback_query_handler(lambda c: c.data == 'no')
async def press_button(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Вы нажали нет')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton('да', callback_data='yes')
    button_2 = types.InlineKeyboardButton('нет', callback_data='no')
    inline_keyboard.add(button_1, button_2)
    await message.answer('Давай поиграем?', reply_markup=inline_keyboard)

@dp.message_handler(commands=['help'])
async def help_comand(message: types.Message):
    await message.answer(
        """terrt
        fgfgf""")

@dp.message_handler()
async def send_message(message: types.Message):
    
    await message.reply(message.text + 'Начнем заново нажми старт')



if __name__=='__main__':
    executor.start_polling(dp)
