matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
sum = 0
count = 0

for row in matrix:
    for element in row:
        if element > 0 and element % 3 == 0:
            sum += element
            count += 1
if count > 0:
    SA = sum / count
    print(f"Среднее арифметическое {SA}")
else:
    print("Нет подходящих элементов")
