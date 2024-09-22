import telebot;
bot=telebot.TeleBot('8081765980:AAFCil6znm8zAWwWsccIrFHph4q9ZOxO5Hk');
@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text=='/start':
          bot.send_message(message.from_user.id,'Здравствуйте, мой дорогой друг, как тебя зовут?')
    elif message.text.isdigit():
            b=int(message.text)
            c=2024-b
            bot.send_message(message.from_user.id,f'Вы родились в {c} году')
    else:
            a=message.text
            bot.send_message(message.from_user.id,f'Приятно познакомиться, {a}')
            bot.send_message(message.from_user.id,f'{a}, введите свой возраст')
    

        
bot.polling(none_stop=True,interval=0)