# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:

    def __init__(self, data: list):
        self.__data = data.copy()
        self.__shape = (len(self.__data), len(max(self.__data,key=len)))
        if len(min(self.__data, key=len)) != self.__shape[1]:
            self.__reshape()

    @property
    def shape(self):
        return self.__shape

    def __reshape(self):
        for row in self.__data:
            tmp = self.__shape[0] - len(row)
            if tmp:
                row.extend([0 for _ in range(tmp)])

    def __getitem__(self, item):
        return self.__data[item]

    def __add__(self, other):
        try:
            if not isinstance(other, Matrix):
                raise TypeError("Ошибка значений: матрицы имеют разные размеры")
            if self.__shape != other.__shape:
                raise ValueError("Ошибка типов данных: это не матрица")
            return Matrix([[x + y for x, y in zip(n, m)]
                           for n, m in zip(self, other)])
        except ValueError:
            print("Ошибка типов данных: это не матрица")
        except TypeError:
            print("Ошибка значений: матрицы имеют разные размеры")

    def __str__(self):
        # Подсчет максимальной длины каждого столбца
        lengths = []
        for j in range(self.__shape[1]):
            max_len = 0
            for i in range(self.__shape[0]):
                if len(str(self[i][j])) > max_len:
                    max_len = len(str(self[i][j]))
            lengths.append(max_len)

        # Создание результирующей строки
        result = ''
        for i in range(self.__shape[0]):
            string = ''
            for j in range(self.__shape[1]):
                string += str(f'[ {self.__data[i][j]:^{lengths[j]}} ] ')
            result += string + '\n'
        return result[0: -1: 1]


if __name__ == '__main__':
    a = Matrix([[1, 2, 142355], [3, 424354, 2], [5, 6]])
    print(a)
    print(a.shape)
    b = Matrix([[11, 22, 33], [11, 22, 33], [11, 22, 33]])
    print(b)
    print(b.shape)
    c = a + b
    print(c)
    print(c.shape)
