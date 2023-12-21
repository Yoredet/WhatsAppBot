graphic = {'16:00': '+79272973331',
                                  '17:00': '+79272973331',
                                  '19:00': '+79024274552',
           '19:30': '+79024274552',
                                  '20:00': '+79297128025',
                                  '21:00': '+79871548090'}
flag_dubl = ''
to_del_list = []
for time, phone in graphic.items():
    if phone == flag_dubl:
        to_del_list.append(time)
    else:
        flag_dubl = phone
print(graphic)
print(to_del_list)
for i in to_del_list:
    del graphic[i]
print(graphic)