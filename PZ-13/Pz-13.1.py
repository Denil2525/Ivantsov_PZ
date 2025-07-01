#В двумерном списке элементы второго столбца заменить элементами из
#одномерного динамического массива соответствующей размерности.
def replace_col(matrix, col_index, new_value):
    return[
        [row[col] if col != col_index else new_value[i]
         for col in range(len(row))]
         for i, row in enumerate(matrix)
]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
new = [10, 20, 30]
new_matrix = replace_col(matrix, 1, new)
print(new_matrix[0])
print(new_matrix[1])
print(new_matrix[2])
