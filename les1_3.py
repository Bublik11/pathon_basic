# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_answer = input("Введите число:\n>>>")
if user_answer.isdigit():
    user_answer_copy = user_answer
    number = 0
    i = 3
    while i > 0:
        number += int(user_answer_copy)
        user_answer_copy += user_answer
        i -= 1
    print(f"Ответ: {number}")
else:
    print("Вы ввели не число!")
