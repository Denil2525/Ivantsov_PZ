a = input("Введите первое число: ")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")
b = input("Введите второе число: ")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите второе число: ")
if a % 2 == 0 and b % 2 == 0:
    print('Оба числа чётные')
elif a % 2 == 0:
    print('A чётное')
elif b % 2 == 0:
    print('B чётное')
else:
    print('Оба числа не чётные')