import telebot
from telebot import types

bot_token = "6089674486:AAEJE6Vajx0gbnQk6bPJjq98J2Dekrpmio0"

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    # Создаем объект клавиатуры
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    # Создаем кнопки
    button1 = types.InlineKeyboardButton('Кнопка 1', callback_data='button1', switch_inline_query_current_chat='')
    button2 = types.InlineKeyboardButton('Кнопка 2', callback_data='button2', switch_inline_query_current_chat='')
    button3 = types.InlineKeyboardButton('Кнопка 3', callback_data='button3', switch_inline_query_current_chat='')
    button4 = types.InlineKeyboardButton('Кнопка 4', callback_data='button4', switch_inline_query_current_chat='')

    # Добавляем кнопки на клавиатуру
    keyboard.add(button1, button2)
    keyboard.add(button3, button4)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'button1':
        bot.send_message(call.message.chat.id, 'Вы нажали кнопку 1')
    elif call.data == 'button2':
        bot.send_message(call.message.chat.id, 'Вы нажали кнопку 2')
    elif call.data == 'button3':
        bot.send_message(call.message.chat.id, 'Вы нажали кнопку 3')
    elif call.data == 'button4':
        bot.send_message(call.message.chat.id, 'Вы нажали кнопку 4')

bot.polling()
