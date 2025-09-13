import random

rows = 4
cols = 5
matrix = [[random.randint(-10, 20) for _ in range(cols)] for _ in range(rows)]

print("Матрица:")
for row in matrix:
    print(row)

positive_multiples_of_3 = []
for row in matrix:
    for element in row:
        if element > 0 and element % 3 == 0:
            positive_multiples_of_3.append(element)

if positive_multiples_of_3:
    average = sum(positive_multiples_of_3) / len(positive_multiples_of_3)
    print(f"\nПоложительные элементы, кратные 3: {positive_multiples_of_3}")
    print(f"Количество элементов: {len(positive_multiples_of_3)}")
    print(f"Сумма элементов: {sum(positive_multiples_of_3)}")
    print(f"Среднее арифметическое: {average:.2f}")
else:
    print("\nВ матрице нет положительных элементов, кратных 3")