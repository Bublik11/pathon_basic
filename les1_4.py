# 4. Пользователь вводит целое положительное число. Найдите самую большую
# цифру в числе. Для решения используйте цикл while и арифметические операции.

user_answer = input("Введите целое положительное число:\n>>>")
if user_answer.isdigit():
    number = int(user_answer)
    max_numeral = 0
    while number > 0:
        if max_numeral < number % 10:
            max_numeral = number % 10
        number = number // 10
    print(f"Ответ: {max_numeral}")
else:
    print("Вы ввели не число!")
