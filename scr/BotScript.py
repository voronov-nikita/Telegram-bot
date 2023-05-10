import telebot
from telebot import types
import sqlite3 as sql
from messages import MessageText, ButtonText, AudioLink


class Bot():
    def __init__(self, token):
        self.create_data_base()
        self.bot = telebot.TeleBot(token, parse_mode="MARKDOWN")

        self.hello:bool = True

    def create_data_base(self):
        db = sql.connect("UserInfo.db")
        cursor = db.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER,
            UserName TEXT,
            level INTEGER
            )
        """)
        db.commit()

    def add_new_user(self, user_id, name, id_chat):
        db = sql.connect("UserInfo.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        replay =cursor.fetchone()
        if not(replay):
            cursor.execute("""
            INSERT INTO users (id, UserName, level) VALUES (?, ?, ?)
            """, (int(user_id), str(name), 1))
            db.commit()
        else:
            self.hello = False
            self.bot.send_message(id_chat, MessageText['replay_start'])

    def run(self):
        # <-------------- Commands for bot -------------->
        @self.bot.message_handler(commands=["start"], content_types=["text"])
        def start_message(message):
            user_id = message.from_user.id
            user_name = message.from_user.username
            self.add_new_user(user_id, user_name, message.chat.id)
            
            if self.hello:
                self.bot.send_message(message.chat.id, MessageText['replay_start'])
            else:
                keyboard = types.ReplyKeyboardMarkup(row_width=2)

                # Создаем кнопки
                button1 = types.KeyboardButton('/find')
                button2 = types.KeyboardButton('/music')
                button3 = types.KeyboardButton('/help')
                button4 = types.KeyboardButton('/more')

                # Добавляем кнопки на клавиатуру
                keyboard.add(button1, button2)
                keyboard.add(button3, button4)
                self.bot.send_message(message.chat.id, MessageText['start'], reply_markup=keyboard)


        @self.bot.message_handler(commands=["help"], content_types=["text"])
        def help_message(message):
            self.bot.send_message(message.chat.id, MessageText['help'])

        @self.bot.message_handler(commands=["music"], content_types=["text"])
        def music_message(message):
            self.bot.send_audio(message.chat.id, AudioLink['first'])

        @self.bot.message_handler(commands=["more"], content_types=["text"])
        def more_message(message):
            # Создаем объект клавиатуры
            keyboard = types.InlineKeyboardMarkup(row_width=2)

            # Создаем кнопки
            button1 = types.InlineKeyboardButton('О создателе', callback_data='btn1', switch_inline_query_current_chat='')
            button2 = types.InlineKeyboardButton('Что это за проект', callback_data='btn2', switch_inline_query_current_chat='')
            button3 = types.InlineKeyboardButton('Как работать', callback_data='btn3', switch_inline_query_current_chat='')
            button4 = types.InlineKeyboardButton('Задать вопрос', callback_data='btn4', switch_inline_query_current_chat='')

            keyboard.add(button1, button2)
            keyboard.add(button3, button4)

            self.bot.send_message(message.chat.id, MessageText['more'], reply_markup=keyboard)

        # <------------ Listenning messages ------------>

        @self.bot.message_handler(func=lambda message: True)
        def listen_message(message):
            self.bot.send_message(message.chat.id, message.text)

        @self.bot.callback_query_handler(func=lambda call: True)
        def listen_button_call(call):
            if call.data == 'btn1':
                self.bot.send_message(call.message.chat.id, ButtonText['author'])
            elif call.data == 'btn2':
                self.bot.send_message(call.message.chat.id, ButtonText['about'])
            elif call.data == 'btn3':
                self.bot.send_message(call.message.chat.id, ButtonText['work'])
            elif call.data == 'btn4':
                self.bot.send_message(call.message.chat.id, ButtonText['FAQ'])


        # <-------------- Starting the bot --------------------->
        self.bot.polling(none_stop=True)

