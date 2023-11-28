import telebot
bot = telebot.Telebot("6612681624:AAHGLaWw_wfdsCCX7TbWpBfwuSyJ8Ve9rBw")

@bot.message_handler(commands=["start"])
def main(message):
    bot send_message(message.chat.id, "Я ждал вас… мои бедные овечки. Да. Этот взгляд! В этом выражении человеческого лица мгновенная надежда превращается в отчаяние. Вот почему я не могу перестать играть в эту маленькую игру/ \nТак зачем я вызвал тебя к себе? \nНе могу всопнить... Хи-хи-хи. \nИспользуй комманды ниже и, так уж и быть, я отвечу тебе. \n\konichiwa \n\tubik \nichinoseguren \n\family \n\mika \n\boring")

@bot.message_handler(commands=["konichiwa"])
def main(message):
    bot send_message(message.chat.id, "Давно не виделись. Ты как всегда прекрасна. \nУлыбаюсь я только из-за любви к тебе")

@bot.message_handler(commands=["tubik"])
def main(message):
    bot send_message(message.chat.id, "Так-так-так, слово ТЮБИК. Посмотрим в словаре. \nЗдесь написано, что это Хиираги Сэйширо... А кто это?")

@bot.message_handler(commands=["ichinoseguren"])
def main(message):
    bot send_message(message.chat.id, "*Как оскорбительно.* Всем известно, что я больше всего на свете ненавижу дураков, которые предают своих товарищей", parse_mode="Markdown")

@bot.message_handler(commands=["family"])
def main(message):
    bot send_message(message.chat.id, "Как говорила принцесса Мики, Кому нужна эта дурацкая «семья»? Меня отправили сюда, потому что мой отец пытался меня убить. Моя мама продолжала разглагольствовать и бредить о том, что я демоническое отродье. В конце концов она сошла с ума и покончила с собой. Так ты понял это сейчас? «Семья» для меня ничего не значит». Конец цитаты. \nИнтересно, почему он тогда так расстроился, когда я избавил его от тех надоедливых детей? *Хахаха*", parse_mode="Markdown")

@bot.message_handler(commands=["mika"])
def main(message):
    bot send_message(message.chat.id, "Мика... Мика... Ми... Мика... Хм-ха-ха")

@bot.message_handler(commands=["boring"])
def main(message):
    bot send_message(message.chat.id, "Боже, жить вечно иногда так скучно. \nТебе, конечно, не понять, но... *[Можешь отлично повеселиться здесь]* Хи-хи-хи (https://mangalib.me/owari_no_seraph?section=info)", parse_mode="Markdown")

bot.infinity_polling()
