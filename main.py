import telebot
bot = telebot.TeleBot('6886487380:AAFSQR3nZYKF_6BjtMjA5OB5lMZ3RAqoNsQ')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет,я могу немного рассказать о себе, если хотите узнать, введите /name')

@bot.message_handler(commands=['name'])
def main(message):
    bot.send_message(message.chat.id, 'Мне 1 день, \nЯ был написан на языке Python \nБольше информации нету),Введите /run,если хотите узнать о языке Python.')
                     
@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, 'Python можно описать одним предложением:Высокоуровневый, интерпретируемый, объектно-ориентированный, императивный, строго типизированный язык общего назначения, который имеет динамическую типизацию.')
    
bot.infinity_polling()

    
                     
