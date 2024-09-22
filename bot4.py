import telebot;
bot=telebot.TeleBot('8081765980:AAFCil6znm8zAWwWsccIrFHph4q9ZOxO5Hk');
name = '';
surname = '';
age = 0;
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Здравствуйте, мой дорогой друг, как тебя зовут?");
        bot.register_next_step_handler(message, get_name);
    else:
        bot.send_message(message.from_user.id, 'Не понимаю Вас. Напишите /start');

def get_name(message):
    name = message.text;
    bot.send_message(message.from_user.id, f'{name}, Введите свой возраст?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age
    while age == 0: 
        try:
             age = int(message.text)
             b=2024-age
        except Exception:
             bot.send_message(message.from_user.id, 'Введите цифры');
    bot.send_message(message.from_user.id, f'{name} ты родился в {b} году')    

        
bot.polling(none_stop=True,interval=0)