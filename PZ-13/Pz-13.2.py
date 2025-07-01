#В двумерном списке найти среднее арифметическое положительных элементов,
#кратных 3
from functools import reduce
def cal_SA(matrix):
    filtered = [
        element
        for row in matrix
        for element in row
        if element > 0 and element % 3 == 0
    ]
    if not filtered:
        return None
    return reduce(lambda x, y: x + y, filtered) / len(filtered)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
SA = cal_SA(matrix)
print(f"Среднее арифметическое {SA}")

