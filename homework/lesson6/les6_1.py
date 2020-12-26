# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time


class TrafficLight:
    __colors = {
        "Red": 7,
        "Yellow": 2,
        "Green": 5
    }

    def __init__(self):
        """
        time_check - абсолютное время выполнения режима светофора
        color - цвет светофора в данный момент времени
        """
        self.__time_check = None
        self.__color = None
        print("Создан новый светофор.\n")

    def running(self):
        """
        Запуск светофора
        :return:
        """
        print("Светофор запущен.\n")
        self.__time_check = time.time()

        while True:
            for key in self.__colors:
                # абсолютное время
                self.__time_check += self.__colors[key]
                # относительное время
                t_stop = time.time() + self.__colors[key]

                if self.__is_correct_time(t_stop):
                    self.__color = key
                    print(f"{self.__color}\n")
                    while t_stop > time.time():
                        continue
                else:
                    print("Время сбилось более чем на 1 секунду. Выход из программы...\n")
                    exit()

    def __is_correct_time(self, t_stop: float):
        """
        Проверка погрешности.
        :param t_stop: float - относительное время до следующего режима светофора
        :return: bool
        """
        print(f"time check: {self.__time_check} | next color time: {t_stop}")
        print(f"time check: {int(self.__time_check)} | next color time: {int(t_stop)}\n")
        return int(self.__time_check) == int(t_stop)


tl = TrafficLight()
tl.running()
