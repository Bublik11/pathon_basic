# 1. Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год». В рамках
# класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу
# «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class MyDate:
    def __init__(self, day_month_year: str) -> None:
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        return tuple([int(el) for el in day_month_year.split('-')])

    @staticmethod
    def valid(day: int, month: int, year: int) -> str:
        t = int(not year % 400 or (year % 100 and not year % 4))
        day_in_month = (31, 28 + t, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        if not 0 < month < 13:
            return 'Неправильный месяц'
        if not 0 < day <= day_in_month[month - 1]:
            return 'Неправильный день'
        return 'Всё правильно'


msg = '29-02-2021'
print(msg, '-', MyDate.valid(*MyDate.extract(msg)))
msg = '29-02-2020'
print(msg, '-', MyDate.valid(*MyDate.extract(msg)))
msg = '29-13-2020'
print(msg, '-', MyDate.valid(*MyDate.extract(msg)))
msg = '32-12-2020'
print(msg, '-', MyDate.valid(*MyDate.extract(msg)))
