name = input("Введите Ваше имя:\n>>>")
surname = input("Введите Вашу фамилию:\n>>>")
patronymic = input("Введите Ваше отчество:\n>>>")
age = input("Сколько Вам лет?\n>>>")
if not age.isdigit():
    print("Ошибка: Вы ввели не число!")
else:
    print(f"Добро пожаловать, {surname} {name} {patronymic}!")
