# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию
# деления на нуль. Проверьте его работу на данных, вводимых пользо-
# вателем. При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByZero(Exception):
    def __init__(self, text):
        self.txt = text


for num in range(3):
    try:
        print('#'*50, f'\nВам доступно {3 - num} выражение(-я).')
        a = int(input("Введите делимое: "))
        b = int(input("Введите делитель: "))
        if b == 0:
            raise DivisionByZero('Ошибка: деление на ноль')
        print(f'a / b = {a / b}')
    except ValueError:
        print('Ошибка: это не число')
    except DivisionByZero as err:
        print(err)
