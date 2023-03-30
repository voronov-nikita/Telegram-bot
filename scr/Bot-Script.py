import sqlite3 as sql
import requests
import telebot
from collecting_data import SendRequest


list_command = [
    ["!all", "!!al"],
    ["none"],
    [str(i) for i in range(1, 10)]
]

token_bot = "6089674486:AAEJE6Vajx0gbnQk6bPJjq98J2Dekrpmio0"
bot = telebot.TeleBot(token_bot, parse_mode="MARKDOWN")


@bot.message_handler(commands=[f'start'], content_types=["text"])
def start_function(message):
    message2 = message
    bot.send_message(message.chat.id, "Привет, прежде чем начать работу, напишите ваше ФИО и класс."
                                      "\nПример: Воронов Никита Рустамович 10А")


@bot.message_handler(commands=['help', 'about'], content_types=['text'])
def write_about_bot(message):
    with open("text_about_bot.txt", "rb") as text:
        bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def write_about_bot(message):
    msg = message.text.lower()

    user_id = message.chat.id

    if msg in list_command[0]:
        bot.send_message(user_id, "OK")
    elif msg in list_command[1]:
        bot.send_message(user_id, "KO")
    elif msg in list_command[2]:
        bot.send_message(user_id, "LLL")
    else:
        bot.send_message(user_id, "Такой команды нет")


# запуск бота
bot.polling(none_stop=True)
