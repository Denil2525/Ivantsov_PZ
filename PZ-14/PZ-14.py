import re

# Открываем файл и читаем текст
with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Регулярное выражение для поиска всех вариантов фамилии Достоевского
pattern = r'Достоевск(ий|ого|ому|им|ом|ая|ой|ую|ие|их|ими)\b'

# Находим все уникальные вхождения
matches = re.findall(pattern, text, flags=re.IGNORECASE)

# Создаем полные варианты фамилий
found_variants = set()
for ending in matches:
    full_surname = 'Достоевск' + ending
    found_variants.add(full_surname)

# Выводим результаты
print("Найденные варианты фамилии Достоевского:")
for i, variant in enumerate(sorted(found_variants), 1):
    print(f"{i}. {variant}")

print(f"\nВсего найдено вариантов: {len(found_variants)}")