import telebot
import random
from telebot import StateMemoryStorage

state_storage = StateMemoryStorage()

bot = telebot.TeleBot("1684742732:AAGZK2_5gx7HcuvgCOgJYFQTeytZu_MalXk")
random_button = "Случайное число"
picture_button = "Картинка"
link_button = "Сслыка"

menu_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
menu_keyboard.add(
    telebot.types.KeyboardButton(random_button),
    telebot.types.KeyboardButton(picture_button),
    telebot.types.KeyboardButton(link_button)
)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот с разным функционалом.")

    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: message.text == random_button)
def handle_random_number(message):
    random_number = random.randint(0, 100)

    bot.send_message(message.chat.id, f"Случайное число: {random_number}")


@bot.message_handler(func=lambda message: message.text == picture_button)
def handle_picture(message):
    photo_url = "https://cdn.forbes.ru/forbes-static/new/2023/04/Dmitrij-Danilov2-643d09737e540.jpg?v=1684996253082"
    bot.send_photo(message.chat.id, photo_url, caption="")

@bot.message_handler(func=lambda message: message.text == link_button)
def handle_google_link(message):
    google_link = "https://www.google.com"
    bot.send_message(message.chat.id, f"Ссылка на Google: {google_link}")

bot.infinity_polling()
