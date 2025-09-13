import tkinter as tk
from tkinter import ttk

# Создание главного окна
root = tk.Tk()
root.title("Sign Up")
root.geometry("500x650")
root.resizable(False, False)

# Основной фрейм
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0,)

# Заголовок
title_label = ttk.Label(main_frame, text="Sign Up", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Имя
ttk.Label(main_frame, text="First Name").grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
first_name = ttk.Entry(main_frame, width=30)
first_name.grid(row=1, column=1, pady=(0, 5))
first_name.insert(0, "Enter First Name...")

# Фамилия
ttk.Label(main_frame, text="Last Name").grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
last_name = ttk.Entry(main_frame, width=30)
last_name.grid(row=2, column=1, pady=(0, 5))
last_name.insert(0, "Enter Last Name...")

# Имя пользователя
ttk.Label(main_frame, text="Screen Name").grid(row=3, column=0, sticky=tk.W, pady=(0, 5))
screen_name = ttk.Entry(main_frame, width=30)
screen_name.grid(row=3, column=1, pady=(0, 5))
screen_name.insert(0, "Enter Screen Name...")

# Дата рождения
ttk.Label(main_frame, text="Date of Birth").grid(row=4, column=0, sticky=tk.W, pady=(0, 5))

dob_frame = ttk.Frame(main_frame)
dob_frame.grid(row=4, column=1, pady=(0, 5))

month_var = tk.StringVar()
day_var = tk.StringVar()
year_var = tk.StringVar()

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_combo = ttk.Combobox(dob_frame, textvariable=month_var, values=months, width=8, state="readonly")
month_combo.set("May")
month_combo.grid(row=0, column=0, padx=(0, 5))

days = [str(i) for i in range(1, 32)]
day_combo = ttk.Combobox(dob_frame, textvariable=day_var, values=days, width=5, state="readonly")
day_combo.set("5")
day_combo.grid(row=0, column=1, padx=(0, 5))

years = [str(i) for i in range(1920, 2023)]
year_combo = ttk.Combobox(dob_frame, textvariable=year_var, values=years, width=6, state="readonly")
year_combo.set("1985")
year_combo.grid(row=0, column=2)

# Пол
ttk.Label(main_frame, text="Gender").grid(row=5, column=0, sticky=tk.W, pady=(0, 5))
gender_frame = ttk.Frame(main_frame)
gender_frame.grid(row=5, column=1, sticky=tk.W, pady=(0, 5))

gender_var = tk.StringVar(value="Male")
ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").grid(row=0, column=0)
ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").grid(row=0, column=1, padx=(10, 0))

# Страна
ttk.Label(main_frame, text="Country").grid(row=6, column=0, sticky=tk.W, pady=(0, 5))
country_var = tk.StringVar()
countries = ["USA", "Canada", "UK", "Australia", "Germany", "France", "Other"]
country_combo = ttk.Combobox(main_frame, textvariable=country_var, values=countries, width=28, state="readonly")
country_combo.set("USA")
country_combo.grid(row=6, column=1, pady=(0, 5))

# Email
ttk.Label(main_frame, text="E-mail").grid(row=7, column=0, sticky=tk.W, pady=(0, 5))
email = ttk.Entry(main_frame, width=30)
email.grid(row=7, column=1, pady=(0, 5))
email.insert(0, "Enter E-mail......")

# Телефон
ttk.Label(main_frame, text="Phone").grid(row=8, column=0, sticky=tk.W, pady=(0, 5))
phone = ttk.Entry(main_frame, width=30)
phone.grid(row=8, column=1, pady=(0, 5))
phone.insert(0, "Enter Phone......")

# Пароль
ttk.Label(main_frame, text="Password").grid(row=9, column=0, sticky=tk.W, pady=(0, 5))
password = ttk.Entry(main_frame, width=30, show="*")
password.grid(row=9, column=1, pady=(0, 5))

# Подтверждение пароля
ttk.Label(main_frame, text="Confirm Password").grid(row=10, column=0, sticky=tk.W, pady=(0, 5))
confirm_password = ttk.Entry(main_frame, width=30, show="*")
confirm_password.grid(row=10, column=1, pady=(0, 5))

# Соглашение с условиями
terms_var = tk.BooleanVar()
terms_check = ttk.Checkbutton(main_frame, text="I agree to the Terms of Use", variable=terms_var)
terms_check.grid(row=11, column=0, columnspan=2, pady=(10, 20))

# Фрейм для кнопок
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=12, column=0, columnspan=2, pady=(0, 10))


# Кнопки
ttk.Button(button_frame, text="Submit").grid(row=0, column=0, padx=(0, 10))
ttk.Button(button_frame, text="Cancel").grid(row=0, column=1)

# Настройка весов сетки
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

# Запуск главного цикла
root.mainloop()
