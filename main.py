import telebot
bot = telebot.TeleBot('6679093324:AAGSrfgrPB_-Lq1uDfAINlBEcYKEkB3KkIs')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '*Привет. \nНачнём общение!*', parse_mode='Markdown')
    
@bot.message_handler(commands=['deal'])
def main(message):
    bot.send_message(message.chat.id, 'У меня всё хорошо. \nА у тебя?')
    
@bot.message_handler(commands=['fine'])
def main(message):
    bot.send_message(message.chat.id, 'Рад за тебя!')
    
@bot.message_handler(commands=['bedly'])
def main(message):
    bot.send_message(message.chat.id, 'Очень жаль...')
    
@bot.message_handler(commands=['over'])
def main(message):
    bot.send_message(message.chat.id, '*Спасибо за общение!*', parse_mode='Markdown')
    
bot.infinity_polling()
