# 2. Пользователь вводит время в секундах. Переведите время
# в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

number_seconds = input("Введите количество секунд:\n>>>")
if number_seconds.isdigit():
    number_seconds = int(number_seconds)
    seconds = number_seconds % 60
    minutes = number_seconds // 60
    hours = minutes // 60
    minutes %= 60
    print(f"{hours}:{minutes}:{seconds}")
else:
    print("Вы ввели не число!")
