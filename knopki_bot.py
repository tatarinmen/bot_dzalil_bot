from aiogram import Bot, Dispatcher, executor, types
 
API_TOKEN = '8081765980:AAFCil6znm8zAWwWsccIrFHph4q9ZOxO5Hk'
 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
 

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   kb = [
       [
           types.KeyboardButton(text="Сможешь повторить это?"),
           types.KeyboardButton(text="А это?")
       ],
   ]
   keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
 
   await message.reply("Привет!\nЯ Эхобот от Skillbox!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.", reply_markup=keyboard)