import telebot
import sqlite3 as sql

class Bot():
    def __init__(self, token):
        self.create_data_base()
        self.bot = telebot.TeleBot(token, parse_mode="MARKDOWN")

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

    def add_new_user(self, id, name):
        db = sql.connect("UserInfo.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user WHERE id=? AND UserName=?", (id, name))
        replay =cursor.fetchone()
        if not(replay):
            cursor.execute("""
            INSERT INTO user (id, UserName, level) VALUES (?, ?, ?)
            """, (int(id), str(name), 1))
            db.commit()

    def run(self):
        @self.bot.message_handler(commands=["start"], content_types=["text"])
        def start_message(message):
            user_id = message.from_user.id
            user_name = message.from_user.username
            self.add_new_user(user_id, user_name)
            
            self.bot.send_message(message.chat.id, "HELLO")

        self.bot.polling(none_stop=True)
