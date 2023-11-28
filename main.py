import telebot
bot = telebot.TeleBot('6755039947:AAEPQR5DGY95hHCSqwhBWu69wWg0lG4txsM')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'шанс получить макбук равны *0,00066666666* \n или *1 к 1500*', parse_mode='Markdown')
    
@bot.message_handler(commands=['omg'])
def main(message):
    bot.send_message(message.chat.id, 'это моя реакция если я получу макбук', parse_mode='Markdown')

bot.infinity_polling()
