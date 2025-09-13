import sqlite3

# Создание базы данных и таблицы
conn = sqlite3.connect('academic_plan.db')
cursor = conn.cursor()

# Создание таблицы Дисциплины
cursor.execute('''
CREATE TABLE IF NOT EXISTS Disciplines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    specialty TEXT NOT NULL,
    lectures INTEGER DEFAULT 0,
    practical INTEGER DEFAULT 0,
    laboratory INTEGER DEFAULT 0,
    assessment_form TEXT NOT NULL
)
''')

# Вставка 10 позиций
disciplines = [
    ('MATH101', 'Высшая математика', 'Информатика', 60, 30, 20, 'Экзамен'),
    ('PHYS201', 'Физика', 'Информатика', 50, 25, 15, 'Экзамен'),
    ('PROG301', 'Программирование', 'Информатика', 40, 40, 30, 'Зачет'),
    ('DB401', 'Базы данных', 'Информатика', 35, 20, 25, 'Экзамен'),
    ('WEB501', 'Веб-разработка', 'Информатика', 30, 35, 20, 'Зачет'),
    ('ECON102', 'Экономика', 'Экономика', 55, 25, 0, 'Экзамен'),
    ('HIST202', 'История', 'Гуманитарные науки', 45, 20, 0, 'Зачет'),
    ('CHEM302', 'Химия', 'Биотехнологии', 50, 30, 40, 'Экзамен'),
    ('BIO402', 'Биология', 'Биотехнологии', 40, 25, 35, 'Экзамен'),
    ('LANG502', 'Иностранный язык', 'Лингвистика', 30, 40, 0, 'Зачет')
]

cursor.executemany('''
INSERT OR IGNORE INTO Disciplines (code, name, specialty, lectures, practical, laboratory, assessment_form)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', disciplines)

conn.commit()


def show_all_disciplines():
    cursor.execute("SELECT * FROM Disciplines")
    disciplines = cursor.fetchall()
    print("\nВсе дисциплины в базе:")
    for disc in disciplines:
        print(disc)
    return len(disciplines)


initial_count = show_all_disciplines()

# 3 ЗАПРОСА НА ПОИСК
print("\n" + "="*50)
print("ЗАПРОСЫ НА ПОИСК")
print("="*50)

print("1. Дисциплины для специальности 'Информатика':")
cursor.execute("SELECT code, name, lectures, practical, laboratory FROM Disciplines WHERE specialty = ?", ('Информатика',))
for disc in cursor.fetchall():
    print(disc)

print("\n2. Дисциплины с формой отчетности 'Экзамен':")
cursor.execute("SELECT code, name, specialty FROM Disciplines WHERE assessment_form = ?", ('Экзамен',))
for disc in cursor.fetchall():
    print(disc)

print("\n3. Дисциплины с лабораторными работами (>0 часов):")
cursor.execute("SELECT code, name, laboratory FROM Disciplines WHERE laboratory > 0")
for disc in cursor.fetchall():
    print(disc)

print("\n" + "="*50)
print("ЗАПРОСЫ НА УДАЛЕНИЕ")
print("="*50)

print("1. Удаляем дисциплину 'История':")
cursor.execute("DELETE FROM Disciplines WHERE name = ?", ('История',))
conn.commit()
print("Удалено строк:", cursor.rowcount)

print("\n2. Удаляем дисциплины без лабораторных работ:")
cursor.execute("DELETE FROM Disciplines WHERE laboratory = 0")
conn.commit()
print("Удалено строк:", cursor.rowcount)

print("\n3. Удаляем дисциплины специальности 'Лингвистика':")
cursor.execute("DELETE FROM Disciplines WHERE specialty = ?", ('Лингвистика',))
conn.commit()
print("Удалено строк:", cursor.rowcount)

after_delete_count = show_all_disciplines()

print("\n" + "="*50)
print("ЗАПРОСЫ НА РЕДАКТИРОВАНИЕ")
print("="*50)

print("1. Увеличиваем лекции по Программированию:")
cursor.execute('''
UPDATE Disciplines 
SET lectures = 50, practical = 45 
WHERE name = ?''', ('Программирование',))
conn.commit()
print("Обновлено строк:", cursor.rowcount)

print("\n2. Меняем форму отчетности для Физики на 'Зачет':")
cursor.execute('''
UPDATE Disciplines 
SET assessment_form = 'Зачет'
WHERE name = ?''', ('Физика',))
conn.commit()
print("Обновлено строк:", cursor.rowcount)

print("\n3. Увеличиваем лабораторные часы на 10 для всех дисциплин:")
cursor.execute('''
UPDATE Disciplines 
SET laboratory = laboratory + 10 
WHERE laboratory > 0''')
conn.commit()
print("Обновлено строк:", cursor.rowcount)

final_count = show_all_disciplines()

conn.close()