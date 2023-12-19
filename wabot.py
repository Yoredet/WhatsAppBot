import pywhatkit
from time import sleep
from xlsxscan import raspisanie


def send_message_inst():
    for fio_doctor, graphic in raspisanie.items():
        for time, phone in graphic.items():
            message = f'Добрый день! 🦷 Хочу напомнить, что завтра мы ждём Вас в {time}. Стоматология «РЖД Медицина» 2 этаж, 201 кабинет. С ув. Врач-стоматолог {fio_doctor}.✨'
            pywhatkit.sendwhatmsg_instantly(phone_no=graphic[phone],
                                            message=message,
                                            tab_close=True)
            sleep(5)


def main():
    send_message_inst()


if __name__ == '__main__':
    main()
