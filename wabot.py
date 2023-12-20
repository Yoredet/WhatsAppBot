import pywhatkit
from time import sleep
from telegrambot import raspisanie, filename
import os


def send_message_inst():
    for fio_doctor, graphic in raspisanie.items():
        for time, phone in graphic.items():
            message = f'Добрый день! 🦷 Хочу напомнить, что завтра мы ждём Вас в {time}. Стоматология «РЖД Медицина» 2 этаж, 201 кабинет. С ув. Врач-стоматолог {fio_doctor}.✨'
            pywhatkit.sendwhatmsg_instantly(phone_no=phone,
                                            message=message,
                                            tab_close=True)
            sleep(5)
    if os.path.isfile(filename):
        os.remove(filename)


def main():
    send_message_inst()
