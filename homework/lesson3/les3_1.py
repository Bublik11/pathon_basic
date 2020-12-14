# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


from les3_add_task import read_float


def division(num1: float, num2: float) -> float:
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
        if num1 < 0:
            return float("-inf")
        else:
            return float("inf")
    else:
        return result


number1 = read_float(add_message="делимое")
number2 = read_float(add_message="делитель")
print(division(number1, number2))

