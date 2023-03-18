import sqlite3 as sql
import requests
import telebot
from collecting_data import SendRequestMOS


list_command = [
    # домашка
    ["домашка", "дз", "домашнее задание"],
    # что-то
    [],
    []
]

token_bot = "6089674486:AAEJE6Vajx0gbnQk6bPJjq98J2Dekrpmio0"
bot = telebot.TeleBot(token_bot, parse_mode="MARKDOWN")


@bot.message_handler(commands=[f'start'], content_types=["text"])
def start_function(message):
    bot.send_message(message.chat.id, "Привет, прежде чем начать работу, напишите ваше ФИО и класс."
                                      "\nПример: Воронов Никита Рустамович 10А")


@bot.message_handler(commands=['help', 'about'], content_types=['text'])
def write_about_bot(message):
    with open("text_about_bot.txt", "rb") as text_about_bot:
        bot.send_message(message.chat.id, text_about_bot)
        print(message.chat.username)


@bot.message_handler(content_types=['text'])
def write_about_bot(message):
    msg = message.text.lower()

    if msg in list_command[0]:
        SendRequestMOS.get_homework()


# запуск бота
bot.polling(none_stop=True)
