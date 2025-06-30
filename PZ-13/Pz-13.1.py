matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
new_col = [10, 20, 30]
k = 1

if len(new_col) == len(matrix) and len(matrix[0]) > k:
    for i in range(len(matrix)):
        matrix[i][k] = new_col[i]
else: print("Ошибка")

print(matrix[0])
print(matrix[1])
print(matrix[2])
