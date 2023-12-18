import openpyxl as op
import re

filename = 'Книга1.xlsx'

wb = op.load_workbook(filename, data_only=True)
sheet = wb.active
raspisanie = {}
for i in range(7, 15):
    time = sheet.cell(row=i, column=5).value
    phone_number = sheet.cell(row=i, column=20).value
    if not time:
        continue
    phone = '+7' + re.sub(r'\W', '', phone_number)[1:]
    raspisanie[time] = phone
flag = ''
for time, phone in raspisanie.items():
    if phone == flag:
        del raspisanie[time]
    else:
        flag = phone
print(raspisanie)