a = float(input("a ="))
s = 0
k = 1
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("a =")
while a < k:
    try:
        a >= k
    except ValueError:
        print("Не может быть меньше одного!")
        a = input("a =")
while s < a:
    s = s+1/k
    k = k+1
print('Количество чисел: ', k)