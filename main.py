import telebot
bot = telebot.TeleBot('6424481048:AAHAbiskuJtXC_PiCWzBHiNS8Gjq7A8_NxM')
 
@bot.message_handler(commands=['/prediction1'])
def main(message):
    bot.send_message(message.chat.id, 'вам всегда будет светить солнце и ваши дни будут полны красок', parse_mode='Markdown')

@bot.message_handler(commands=['/prediction2'])
def main(message):
    bot.send_message(message.chat.id, 'сияние звезд озарит вам путь и укажет верное направление', parse_mode='Markdown')

@bot.message_handler(commands=['/prediction3'])
def main(message):
    bot.send_message(message.chat.id, 'для вас успех и слава, равносильно смене дня и ночи ', parse_mode='Markdown')
    
bot.infinity_polling()
