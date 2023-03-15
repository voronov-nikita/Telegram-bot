import sqlite3 as sql
import requests
import telebot

token_bot = "6089674486:AAEJE6Vajx0gbnQk6bPJjq98J2Dekrpmio0"
bot = telebot.TeleBot(token_bot, parse_mode="MARKDOWN")

db = sql.connect("info.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS table_info(
    nik TEXT,
    name TEXT,
    surname TEXT,
    patronymic TEXT,
    class TEXT
)
""")
db.commit()


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
    get_message_chat = message.json['text']
    if len(get_message_chat.split()) == 3:
        print('ok')


bot.polling(none_stop=True)

