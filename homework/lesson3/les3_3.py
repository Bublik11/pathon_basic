# 3. Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.


from les3_add_task import read_float


def my_funk(num1, num2, num3):
    return sum((num1, num2, num3)) - min(num1, num2, num3)


a = read_float(add_message="число №1")
b = read_float(add_message="число №2")
c = read_float(add_message="число №2")
print("Сумма наибольших двух чисел:", my_funk(a, b, c))
