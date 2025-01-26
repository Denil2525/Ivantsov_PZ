#Дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N 
c = 1
r = 0
b = input("Введите число: ")
while type(b) != int: # обработка исключений
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите второе число: ")
k = 0
a = 1
while c <= b:
    c += 1
    k += 1
    r += a / k
print(r)
