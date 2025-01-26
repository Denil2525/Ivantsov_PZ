#Составить программу, в которой функция генерирует четырехзначное число и 
#определяет, есть ли в числе одинаковые цифры.
import random
def Rand4():
    number = random.randint(1000, 9999)
    number = str(number)
    print(number)
    if number[0] == number[1] or number[0] == number[2] or number[0] == number[3]:
        print("Да, в числе есть две одинаковые цифры.")
    elif number[1] == number[2] or number[1] == number[3]:
        print("Да, в числе есть две одинаковые цифры.")
    elif number[2] == number[3]:
        print("Да, в числе есть две одинаковые цифры.")
    else:
        print("Нет, в числе нет двух одинаковых цифр.")
Rand4()
