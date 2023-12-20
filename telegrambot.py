import openpyxl as op
import os
from pprint import pprint
import re
import pywhatkit
from secret import TOKEN
import telebot
from time import sleep


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message, 'Понял, принял')
    photo_info = message.photo[-1]
    file_id = photo_info.file_id
    file_object = bot.get_file(file_id)
    file_bytes = bot.download_file(file_object.file_path)
    target_file_name = "test.jpg"
    with open(target_file_name, 'wb') as writer:
        writer.write(file_bytes)


@bot.message_handler(content_types=['document'])
def handle_file(message):
    global file_name
    file_name = message.document.file_name
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, 'Табличку получил')
    bot.send_message(message.chat.id, 'Ок')
    bot.stop_polling()


bot.polling()


def parsing_file():
    wb = op.load_workbook(file_name, data_only=True)
    sheet = wb.active
    max_rows = sheet.max_row
    for i in range(7, max_rows+1):
        time = sheet.cell(row=i, column=5).value
        phone_number = sheet.cell(row=i, column=20).value
        yes_no_flag = sheet.cell(row=i, column=4).value
        fio = str(sheet.cell(row=i, column=15).value)
        fio_doctor = re.sub(r'[^\w\s]+|[\d]+', r'', fio).strip().title()
        if not time or yes_no_flag == 'ДА' or not phone_number or \
                phone_number[3] != '9' or len(phone_number) != 17:
            continue
        phone = '+7' + re.sub(r'\W', '', phone_number)[1:]
        in_dict = {}
        in_dict[time] = phone
        if fio_doctor not in raspisanie:
            raspisanie[fio_doctor] = in_dict
        else:
            raspisanie[fio_doctor][time] = phone
    flag_dubl = ''

    for fio, graphic in raspisanie.items():
        for time, phone in graphic.items():
            if phone == flag_dubl:
                del graphic[time]
            else:
                flag_dubl = phone


raspisanie = {}

parsing_file()
pprint(raspisanie)


def send_message_inst():
    for fio_doctor, graphic in raspisanie.items():
        for time, phone in graphic.items():
            message = f'Добрый день! 🦷 Хочу напомнить, что завтра мы ждём Вас в {time}. Стоматология «РЖД Медицина» 2 этаж, 201 кабинет. С уважением Врач-стоматолог {fio_doctor}.✨'
            pywhatkit.sendwhatmsg_instantly(phone_no=phone,
                                            message=message,
                                            tab_close=True)
            sleep(5)


def main():
    send_message_inst()
    if os.path.isfile(file_name):
        os.remove(file_name)


main()
