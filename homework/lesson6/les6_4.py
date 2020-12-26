# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина ({type(self)}) {self.name} поехала")

    def stop(self):
        print(f"Машина ({type(self)}) {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина ({type(self)}) {self.name} повернула {direction}")

    def show_speed(self):
        print(f"У машины ({type(self)}) {self.name} на данный момент скорость: {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super(TownCar, self).__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print(f"У машины ({type(self)}) {self.name} превышена скорость! ({self.speed})")
        else:
            print(f"У машины ({type(self)}) {self.name} на данный момент скорость: {self.speed}")


class SportCar(Car):
    def __init__(self, speed, max_speed, color, name):
        super(SportCar, self).__init__(speed, color, name)
        self._max_speed = max_speed

    def get_max_speed(self):
        return self._max_speed


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super(WorkCar, self).__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print(f"У машины ({type(self)}) {self.name} превышена скорость! ({self.speed})")
        else:
            print(f"У машины ({type(self)}) {self.name} на данный момент скорость: {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super(PoliceCar, self).__init__(speed, color, name, True)


car1 = TownCar(60, 'yellow', '423oo')
car2 = SportCar(50, 250, 'blue', 'e324oн')
car3 = WorkCar(70, 'red', 'e421oy')
car4 = PoliceCar(60, 'white', 'e382ox')
print()

car1.show_speed()
car2.show_speed()
car3.show_speed()
car4.show_speed()
print()

car1.stop()
car1.go()
print()

print(f"Максимальная скорость {car2.name} = {car2.get_max_speed()}")
print(f"Скорость {car2.name} = {car2.speed}")
print(f"{type(car4)} это машина полиции? {car4.is_police}")
print(f"{type(car1)} это машина полиции? {car1.is_police}")
