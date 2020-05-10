#!venv/bin/python
# -*- coding: utf-8 -*-

import config
import telebot
import logging
import os
from telebot import types
from flask import Flask, request

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start')
    start_text = str('Привет, ' + message.from_user.first_name + '!\nЯ бот на Heroku.')
    bot.send_message(message.chat.id, text=start_text, parse_mode='Markdown')


@bot.message_handler(commands=['enter'])
def command_enter(message):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, text='Твой Председатель: у тебя что-то срочное?', reply_markup=markup)
    button1 = types.InlineKeyboardButton('Да', callback_data="b1")
    button2 = types.InlineKeyboardButton('Пойдем курить', callback_data="b2")
    button3 = types.InlineKeyboardButton('Куда положить печенье?', callback_data="b3")
    button4 = types.InlineKeyboardButton('Как принимать матпомощь?', callback_data="b4")
    button5 = types.InlineKeyboardButton('* молча вышел *', callback_data="b5")
    markup.add(button1, button2, button3, button4, button5)


@bot.callback_query_handler(func=lambda call:True)
def callback_worker(call):
    try:
        if call.message:
            if call.data == "b1":
                bot.send_message(call.message.from_user.id, text='Слушаю', reply_markup=None)
            if call.data == "b2":
                bot.send_message(call.message.from_user.id, text='Стартуем', reply_markup=None)
            if call.data == "b3":
                bot.send_message(call.message.from_user.id, text='* BOOM *', reply_markup=None)
            if call.data == "b4":
                bot.send_message(call.message.from_user.id, text='К Оле Гончаровой', reply_markup=None)
            if call.data == "b5":
                bot.send_message(call.message.from_user.id, text='У нас так не принято', reply_markup=None)
    except Exception as e:
        print(repr(e))


if "HEROKU" in list(os.environ.keys()):
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = Flask(__name__)

    @server.route('/' + bot, methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200

    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url='https://dashboard.heroku.com/apps/prbot1')
        return "?", 200
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))  # либо порт 80

else:
    bot.remove_webhook()
    bot.polling(none_stop=True)

# if __name__ == '__main__':
    # server.debug = True
   #  server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))



# if __name__ == '__main__':
#    bot.polling(none_stop=True)

