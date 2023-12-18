import pytesseract
import cv2
import re


def scan_image():
    img = cv2.imread('test.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    config = r'--oem 3 --psm 6'

    text = pytesseract.image_to_string(img, lang='rus', config=config)
    print(text)
    return text


def crop_and_make_dict():
    result_time = re.findall(r"(\d{2}\:00)", scan_image())
    result_numbers = re.findall(r"[(]\d{3}[)]\s\d{3}-\d{2}-\d{2}", scan_image())
    print(result_time)
    print(result_numbers)
    new_result_numbers = []
    for i in result_numbers:
        newi = re.sub(r'\W', '', i)
        newi = '+7' + newi
        new_result_numbers.append(newi)

    raspisanie = dict(zip(result_time, new_result_numbers))
    return raspisanie


result = crop_and_make_dict()
print(result)
