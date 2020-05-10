#!venv/bin/python
# -*- coding: utf-8 -*-

import config
import telebot
import logging
import telegram
from telebot import types

token = '1194351305:AAGZdRZJF97JXCbvIJY9tsZcPO__nJSOYf0'
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['enter'])
def command_enter(message):
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, text='Твой Председатель: у тебя что-то срочное?', reply_markup=markup)
    button1 = types.InlineKeyboardButton('Да', callback_data='b1')
    button2 = types.InlineKeyboardButton('Пойдем курить', callback_data='b2')
    button3 = types.InlineKeyboardButton('Куда положить печенье?', callback_data='b3')
    button4 = types.InlineKeyboardButton('Как принимать матпомощь?', callback_data='b4')
    button5 = types.InlineKeyboardButton('* молча вышел *', callback_data='b5')
    markup.add(button1, button2, button3, button4, button5)

@bot.callback_query_handler(func=lambda call:True)
def callback_worker(call):
    try:
        if call.message:
            if call.data == "b1":
                bot.send_message(call.message.from_user.id, text='Слушаю', reply_markup=None)
            elif call.data == "b2":
                bot.send_message(call.message.from_user.id, text='Стартуем', reply_markup=None)
            elif call.data == "b3":
                bot.send_message(call.message.from_user.id, text='* B O O M *', reply_markup=None)
            elif call.data == "b4":
                bot.send_message(call.message.from_user.id, text='Все вопросы к Оле Гончаровой', reply_markup=None)
            elif call.data == "b5":
                bot.send_message(call.message.from_user.id, text='У нас так не принято -_- ', reply_markup=None)
    except Exception as e:
        print(repr(e))

if __name__ == '__main__':
    bot.polling(none_stop=True)

