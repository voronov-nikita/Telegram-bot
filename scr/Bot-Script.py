import sqlite3 as sql
import requests
import telebot

token_bot = "6089674486:AAEJE6Vajx0gbnQk6bPJjq98J2Dekrpmio0"
bot = telebot.TeleBot(token_bot, parse_mode="MARKDOWN")


@bot.message_handler(commands=['start'], content_types=["text"])
def start_function(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(commands=['help'], content_types=['text'])
def write_about_bot(message):
    with open("text_about_bot.txt", "rb") as text_about_bot:
        bot.send_message(message.chat.id, text_about_bot)


bot.polling(none_stop=True)

