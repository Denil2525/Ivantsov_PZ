from functools import reduce

seq1 = input("Введите первую последовательность (через пробел): ").split()
seq2 = input("Введите вторую последовательность (через пробел): ").split()

# Функциональный подход
common_elements = list(set(seq1) & set(seq2))
count_common = len(common_elements)

# Подсчет общего количества вхождений (минимальное из двух последовательностей для каждого элемента)
total_common_count = reduce(
    lambda acc, elem: acc + min(seq1.count(elem), seq2.count(elem)),
    common_elements,
    0
)

# Вывод результатов
print(f"Общие элементы: {common_elements}")
print(f"Количество различных общих элементов: {count_common}")
print(f"Общее количество вхождений общих элементов: {total_common_count}")