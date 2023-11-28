import telebot
from telebot import types
from datetime import datetime
 
bot = telebot.TeleBot('your_token')
 
 
def get_cat_url():
    return f'https://cataas.com/cat?t={int(datetime.now().timestamp())}'
 
 
@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Котик")
    markup.add(item1)
 
    bot.send_message(message.chat.id, "Привет! Могу тебе отправить милого котика!", reply_markup=markup)
 
 
@bot.message_handler(func=lambda message: True)
def handle_commands(message):
    if message.text == "Котик":
        cat_url = get_cat_url()
        bot.send_photo(message.chat.id, cat_url)
 
 
if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
