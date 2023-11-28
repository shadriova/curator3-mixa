import telebot
bot = telebot.TeleBot('6823637731:AAGBk7Ca_UVnMIHEu3O69xDG7DmK4DiFMo4')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'ПРИВЕТ! \nдля начала работы оплатите бота)')
    
@bot.message_handler(commands=['pay'])
def main(message):
    bot.send_message(message.chat.id, '-500$ \nвы успешно оплатили бота!')
    
@bot.message_handler(commands=['meme'])
def main(message):
    bot.send_message(message.chat.id, '*ТЫК*(https://youtu.be/dQw4w9WgXcQ?si=aJHvo7eFfa6OHYPx)', parse_mode='Markdown')

@bot.message_handler(commands=['joke'])
def main(message):
    bot.send_message(message.chat.id, 'Штирлиц шёл в Дрезден с трудом разбирая дорогу. \nНаутро железная дорога от Берлина до Дрездена была полностью разобрана...',)

@bot.message_handler(commands=['song'])
def main(message):
    bot.send_message(message.chat.id, '*ТЫК*(https://youtu.be/boT7QIGOmbc?si=AC9VetUeUMHdFPDK)', parse_mode='Markdown')

bot.infinity_polling()
