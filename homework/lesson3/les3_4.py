# 4. Программа принимает действительное положительное число x и целое
# отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


import sys
from les3_add_task import read_int


def my_func1(x: int, y: int) -> float:
    if y == 0 or x == 1:
        return 1
    elif x == 0 and y != 0:
        return float("inf")
    else:
        return x**y


def my_func2(x: int, y: int) -> float:
    temp = x

    # чтобы избежать долгого ожидания работы программы при большом числе y
    max_float = sys.float_info.max

    if y == 0 or x == 1:
        return 1
    elif x == 0 and y != 0:
        return float("inf")
    else:
        for i in range(1, abs(y), 1):
            if x >= max_float:
                return 0.0
            x *= temp
        result = 1 / x
        return result


num1 = read_int(is_positive=True, add_message="основание")
num2 = read_int(is_negative=True, add_message="степень")
print("Ответ:", my_func1(num1, num2))
print("Ответ:", my_func2(num1, num2))
