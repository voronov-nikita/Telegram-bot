import telebot
import sqlite3 as sql
from messages import msg

class Bot():
    def __init__(self, token):
        self.create_data_base()
        self.bot = telebot.TeleBot(token, parse_mode="MARKDOWN")

        self.hello:bool = True

    def create_data_base(self):
        db = sql.connect("UserInfo.db")
        cursor = db.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS user(
            id INTEGER,
            UserName TEXT,
            level INTEGER
            )
        """)
        db.commit()

    def add_new_user(self, user_id, name, id_chat):
        db = sql.connect("UserInfo.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user WHERE id=?", (user_id,))
        replay =cursor.fetchone()
        if not(replay):
            cursor.execute("""
            INSERT INTO user (id, UserName, level) VALUES (?, ?, ?)
            """, (int(user_id), str(name), 1))
            db.commit()
        else:
            self.hello = False
            self.bot.send_message(id_chat, msg['replay_start'])

    def run(self):
        # commands for bot
        @self.bot.message_handler(commands=["start"], content_types=["text"])
        def start_message(message):
            user_id = message.from_user.id
            user_name = message.from_user.username
            self.add_new_user(user_id, user_name, message.chat.id)
            
            if self.hello:
                self.bot.send_message(message.chat.id, msg['start'])

        @self.bot.message_handler(commands=["help"], content_types=["text"])
        def help_message(message):
            self.bot.send_message(message.chat.id, msg['help'])

        @self.bot.message_handler(commands=["more"], content_types=["text"])
        def more_message(message):
            self.bot.send_message(message.chat.id, msg['more'])

        # starting the bot
        self.bot.polling(none_stop=True)
