from telebot import types

import telebot

bot = telebot.TeleBot('6260172945:AAHZ860gKsVSD2tOG4oUfwsLAgD8YZkrnXM')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '*Приветствую!* \nДорогой друг', parse_mode='Markdown')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'Присоединяйся [ССЫЛКА](https://youtube.com/)', parse_mode='Markdown')


@bot.message_handler(commands=['text'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Интересный факт!")
    btn2 = types.KeyboardButton("Как дела?")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="И снова здраствуй {0.first_name}!Хочешь узнать *что-то* интересное? ".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Интересный факт!"):
        bot.send_message(message.chat.id, text="Облако средних размеров весит порядка 500 тонн)")
    elif (message.text == "Как дела?"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хорошо")
        btn2 = types.KeyboardButton("Отлично")
        back = types.KeyboardButton("Вернуться")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Как дела?", reply_markup=markup)

    elif (message.text == "Хорошо"):
        bot.send_message(message.chat.id, "Это хорошо).")

    elif message.text == "Отлично":
        bot.send_message(message.chat.id, text="Да ты счастливчик!")

    elif (message.text == "Вернуться"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Интересный факт!")
        button2 = types.KeyboardButton("Как дела?")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись", reply_markup=markup)


bot.infinity_polling()