import random

rows = int(input("Введите количество строк матрицы: "))
cols = int(input("Введите количество столбцов матрицы: "))

matrix = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

print("\nИсходная матрица:")
for row in matrix:
    print(row)

dynamic_array = [random.randint(20, 50) for _ in range(rows)]

print(f"\nДинамический массив: {dynamic_array}")

result_matrix = list(map(lambda row, new_val: row[:1] + [new_val] + row[2:], matrix, dynamic_array))

print("\nРезультирующая матрица:")
for row in result_matrix:
    print(row)