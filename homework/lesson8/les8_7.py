# 7. Реализовать проект «Операции с комплексными числами». Создайте
# класс «Комплексное число», реализуйте перегрузку методов сложения и
# умножения комплексных чисел. Проверьте работу проекта, создав экземп-
# ляры класса (комплексные числа) и выполнив сложение и умножение соз-
# данных экземпляров. Проверьте корректность полученного результата.

class Complex:

    def __init__(self, a: float, b: float):
        self.a = float(a)
        self.b = float(b)

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a*other.a - self.b*other.b,
                       self.a*other.b + self.b*other.a)

    def __str__(self):
        return f'({self.a} + {self.b}*i)'


a = Complex(2, 3)
b = Complex(-1, 1)
print(f'{a} + {b} = {a + b}')
print(f'{a} * {b} = {a * b}')
