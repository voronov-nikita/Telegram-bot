import telebot
from PIL import Image
import io

bot_token = "6089674486:AAEJE6Vajx0gbnQk6bPJjq98J2Dekrpmio0"

def from_bytes(user_id, file):
    stream = io.BytesIO(file)

    # Используем метод open из модуля Image, чтобы открыть изображение из потока данных
    image = Image.open(stream)

    # Теперь вы можете использовать объект image для выполнения дополнительной обработки изображения
    # Например, можно сохранить изображение на диск:
    bot.send_photo(user_id, image)

bot = telebot.TeleBot(bot_token)
ls = []
# Обработка сообщений с изображениями
@bot.message_handler(content_types=['photo'])
def handle_image(message):
    photo = message.photo[-1]  # Берем последнее изображение из списка
    file_id = photo.file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    byte_array = bytearray(downloaded_file)
    ls.append(byte_array)

    # Дальнейшая обработка массива байтов (byte_array)
    # Например, сохранение в базу данных или дальнейшая обработка изображения
    
    # Ответ пользователю
    bot.reply_to(message, 'Изображение принято и обработано')
    from_bytes(message.chat.id, ls[0])

# Запуск бота
bot.polling()
