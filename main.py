import telebot
bot = telebot.TeleBot('6780228993:AAGz261WCaSZXz6RSyYV5ZjBnSVS2rVHwgs')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'НАЧАЛИ!', parse_mode='Markdown')

@bot.message_handler(commands=['hi'])
def main(message):
    bot.send_message(message.chat.id, 'Ну здорова!', parse_mode='Markdown')

@bot.message_handler(commands=['goodbye'])
def main(message):
    bot.send_message(message.chat.id, '_Ну все, покеда._', parse_mode='Markdown')
bot.infinity_polling()
