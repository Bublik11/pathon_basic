# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и
# проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    __count = 0

    def __init__(self):
        super().__init__("ручка")
        Pen.__count += 1
        self.number = Pen.__count

    def draw(self):
        print(f"Запуск отрисовки ({self.title} №{self.number})")


class Pencil(Stationery):

    def __init__(self, dark):
        super().__init__("карандаш")
        self.dark = dark

    def draw(self):
        print(f"Запуск отрисовки ({self.title} {self.dark})")


class Handle(Stationery):

    def __init__(self, color):
        super().__init__("маркер")
        self.color = color

    def draw(self):
        print(f"Запуск отрисовки {self.title} цвет: {self.color}")


pen1 = Pen()
pen2 = Pen()
pen3 = Pen()

pencil1 = Pencil('1B')
pencil2 = Pencil('4B')
pencil3 = Pencil('2B')

handle1 = Handle('Red')
handle2 = Handle('Green')
handle3 = Handle('Blue')

pen1.draw()
pen2.draw()
pen3.draw()
print()

pencil1.draw()
pencil2.draw()
pencil3.draw()
print()

handle1.draw()
handle2.draw()
handle3.draw()
