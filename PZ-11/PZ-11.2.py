# Из предложенного текстового файла (text18-9.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив последнюю строку фразой введенной
# пользователем.

with open('text18-9.txt', 'r', encoding='utf-16') as file:
    content = file.read()

print("Содержимое файла:")
print(content)
print()

lowercase_count = 0
for char in content:
    if char.isalpha() and char.islower():
        lowercase_count += 1

print(f"Количество букв в нижнем регистре: {lowercase_count}")
print()

user_phrase = input("Введите фразу для последней строки: ")

lines = content.split('\n')

with open('новый_файл.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        if line.strip():  
            file.write(line + '\n')
    file.write(user_phrase + '\n')

print("Новый файл создан: 'новый_файл.txt'")
