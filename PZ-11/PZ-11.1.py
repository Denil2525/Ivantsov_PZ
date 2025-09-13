numbers = [5, -3, 8, 12, -7, 4, 9, -2, 15, 6, -1, 10, 3, -5, 7]

# Создаем исходный файл
with open("исходные_данные.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + " ")

# Читаем данные из файла
with open("исходные_данные.txt", "r") as file:
    data = file.read().split()
    numbers = [int(x) for x in data]

# Подсчитываем количество элементов
count = len(numbers)

# Находим индекс последнего максимального элемента
max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num

last_max_index = 0
for i in range(count):
    if numbers[i] == max_value:
        last_max_index = i

# Меняем местами первую и последнюю трети
third = count // 3
first_part = numbers[:third]
middle_part = numbers[third:2*third]
last_part = numbers[2*third:]
swapped = last_part + middle_part + first_part

# Создаем новый файл с результатами
with open("обработанные_данные.txt", "w") as file:
    file.write("Исходные данные:\n")
    file.write(" ".join(str(x) for x in numbers) + "\n")
    file.write(f"Количество элементов: {count}\n")
    file.write(f"Индекс последнего максимального элемента: {last_max_index}\n")
    file.write("Меняем местами первую и последнюю трети:\n")
    file.write(" ".join(str(x) for x in swapped))

print("Файлы успешно созданы!")