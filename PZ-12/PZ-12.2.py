import string

text = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'

# Функциональный подход с использованием библиотеки string
lowercase_chars = list(filter(lambda char: char in string.ascii_lowercase, text))

# Альтернативный вариант с list comprehension
lowercase = [char for char in text if char in string.ascii_lowercase]

# Вывод результатов
print("Символы нижнего регистра:")
print(''.join(lowercase))
print(f"\nКоличество символов нижнего регистра: {len(lowercase)}")