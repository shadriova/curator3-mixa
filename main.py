import telebot

banan = telebot.TeleBot("6859145466:AAEfzbtPJdcqfvv5p_MUGFmACi1DUQt0jQc")


@banan.message_handler(commands=["start"])
def main(message):
    banan.send_message(message.chat.id, 'Артем краш')


@banan.message_handler(commands=["Да ?"])
def main(message):
    banan.send_message(message.chat.id, '*А вы не верили* \n а я уверен в себе', parse_mode='Markdown')


@banan.message_handler(commands=["Нет"])
def main(message):
    banan.send_message(message.chat.id, 'я хотел сделать выбор Да либо Нет ')


banan.infinity_polling()
