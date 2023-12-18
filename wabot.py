import pywhatkit
from time import sleep
from xlsxscan import raspisanie

flag = input('Если вы самый прекрасный на свете стоматолог, то нажмите 1 и энтер, Леша жми любую кнопку')


def send_message_inst():
    for time, mobile in raspisanie.items():
        message_lesha = f'Добрый день! 🦷 Хочу напомнить, что завтра мы ждём Вас в {time}. Стоматология «РЖД Медицина» 2 этаж, 201 кабинет. С ув. Врач-стоматолог Лебедевич А.Д.✨'
        message_nastya = f'Добрый день! 🦷 Хочу напомнить, что завтра мы ждём Вас в {time}. Стоматология «РЖД Медицина» 2 этаж, 204 кабинет. С ув. Врач-стоматолог Лебедевич А.В.✨'
        if flag == 1:
            pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message_nastya)
            sleep(5)
        else:
            pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message_lesha)
            sleep(5)


def main():
    send_message_inst()


if __name__ == '__main__':
    main()
