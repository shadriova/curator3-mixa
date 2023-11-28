import telebot

bot = telebot.TeleBot("6781184184:AAGcoLFW2LY3bH8wQphR61OBPgTwUd4A5S4")

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Здравствуй).')


@bot.message_handler(commands=['beep'])
def main(message):
    bot.send_message(message.chat.id, 'Бип-бип!На связи.')


@bot.message_handler(commands=['bite'])
def main(message):
    bot.send_message(message.chat.id, 'Ай-ой.')


bot.infinity_polling()
