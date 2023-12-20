import sys
import telebot
from secret import TOKEN
bot = telebot.TeleBot(TOKEN)

file_got = False


@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message, 'Понял, принял')
    photo_info = message.photo[-1]
    file_id = photo_info.file_id
    file_object = bot.get_file(file_id)
    file_bytes = bot.download_file(file_object.file_path)
    target_file_name = f"test.jpg"
    with open(target_file_name, 'wb') as writer:
        writer.write(file_bytes)


@bot.message_handler(content_types=['document'])
def handle_file(message):
    file_name = message.document.file_name
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, 'Табличку получил')
    bot.send_message(message.chat.id, 'Ок')
    bot.stop_polling()


bot.polling()
