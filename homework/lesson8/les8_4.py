# 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать пара-
# метры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвеча-
# ющие за приём оргтехники на склад и передачу в определенное подразде-
# ление компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходя-
# щую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валида-
# ции вводимых пользователем данных. Например, для указания количества
# принтеров, отправленных на склад, нельзя использовать строковый тип
# данных.

# Подсказка: постарайтесь по возможности реализовать в проекте «Склад
# оргтехники» максимум возможностей, изученных на уроках по ООП.

from copy import copy
from abc import ABC, abstractmethod


class SignError(Exception):
    """Класс ошибки знака в числе"""
    def __init__(self, text):
        self.txt = text


class Ui:
    @staticmethod
    def pos_number(funk, add_msg='',):
        while True:
            try:
                result = funk(input(add_msg))
                if result <= 0:
                    raise SignError('Ошибка: число не положительное')
                return result
            except ValueError:
                print('Ошибка: введен некорректный тип данных')
            except SignError as msg:
                print(msg)

    @staticmethod
    def help(store, *args, **kwargs):
        content = f'Вам доступны следующие команды:\n' \
                  f'{"help":<10}- Показать команды\n' \
                  f'{"add":<10}- Добавляет объекты на склад.\n' \
                  f'{"":<12}Доступные атрибуты: -p(принтер), ' \
                  f'-s(сканер), -x(МФУ), -d(подразделение)\n' \
                  f'{"show_dep":<10}- Показать все подразделения.\n' \
                  f'{"":<12}Доступные атрибуты: "название подразделения"' \
                  f'(отображение оборудования у подразделения).\n' \
                  f'{"":<12}Например, "show_dep Отдел Связи"\\' \
                  f'"show_dep"\n' \
                  f'{"show_st":<10}- показать технику на складе\n' \
                  f'{"cd":<10}- Передать оборудование.\n' \
                  f'{"":<12}Доступные атрибуты: -g(со склада), ' \
                  f'-t(на склад)\n' \
                  f'{"exit":<10}- Завершение работы программы'
        print(content)
        return store

    @staticmethod
    def add(store, type_yq='', *args, **kwargs):
        try:
            if type_yq == '':
                msg = 'Введите параметр:\n' \
                      '-d : добавить подразделение компании\n' \
                      '-p : добавить принтер на склад\n' \
                      '-s : добавить сканер на склад\n' \
                      '-x : добавить МФУ на склад\n>>>'
                type_yq = input(msg)
            if type_yq not in ('-d', '-p', '-s', '-x'):
                raise ValueError(f'Ошибка: неизвестный параметр "{type_yq}"')
            store.add(type_yq)
        except ValueError as msg:
            print(msg)
        return store

    @staticmethod
    def show_dep(store, name_dep='', *args, **kwargs):
        if name_dep == '':
            store.show_dep()
        elif name_dep in store.office:
            store.show_dep(name_dep)
        else:
            print(f'Ошибка: неизвестное подразделение "{name_dep}"')
        return store

    @staticmethod
    def show_st(store, *args, **kwargs):
        print(store)
        return store

    @staticmethod
    def cd(store, give_take='', *args, **kwargs):
        try:
            if give_take == '':
                msg = 'Введите параметр:\n' \
                      '-g : выдать технику со склада\n' \
                      '-t : вернуть технику на склад\n>>>'
                give_take = input(msg)

            if give_take not in ('-g', '-t'):
                raise ValueError(f'Ошибка: неизвестный параметр "{give_take}"')

            if not store.office:
                raise ValueError(f'Внимание: для выполнения команды '
                                 f'хотя бы одно подрзделение')
            store.show_dep()
            idx_dep = Ui.pos_number(int, 'Выберите порядковый номер подразделения:\n>>>') - 1
            if not 0 <= idx_dep < len(store.office):
                raise IndexError(f'Ошибка: некорректный индекс подразделения: {idx_dep + 1}')
            # преобразовываем индекс в название подразделения
            name_dep = [el for el in store.office][idx_dep]

            tmp_list = None
            if give_take == '-g':
                # показываем технику на складе
                # показываем технику подразделения
                if not store.equipments:
                    raise ValueError(f'Внимание: за подразделением "{store.name}" не числится оборудование')
                print(store)
                give_take = True
                tmp_list = store.equipments
            else:
                # показываем технику подразделения
                if not store.office[name_dep]:
                    raise ValueError(f'Внимание: за подразделением "{name_dep}" не числится оборудование')
                store.show_dep(name_dep)
                give_take = False
                tmp_list = store.office[name_dep]

            idx_eq = Ui.pos_number(int, 'Выберите порядковый номер оборудования:\n>>>') - 1
            if not 0 <= idx_eq < len(tmp_list):
                raise IndexError(f'Ошибка: некорректный индекс оборудования: {idx_eq + 1}')
            num_eq = Ui.pos_number(int, 'Выберите количество передаваемого оборудования:\n>>>')
            if not 0 < num_eq <= tmp_list[idx_eq].number:
                raise ValueError(f'Ошибка: некорректное количество техники: {num_eq}')
            store.give_take_eq(name_dep, idx_eq, num_eq, give_take)

        except ValueError as msg:
            print(msg)
        except IndexError as msg:
            print(msg)
        return store

    @staticmethod
    def exit_app(*args, **kwargs):
        exit()


class Storage:
    def __init__(self, name: str):
        self.name = name
        self.equipments = []
        self.office = {}

    @staticmethod
    def __is_on_list(list_eq: list, name_ey: str, model_eq: str) -> int:
        """
        Проверка на наличие техники в списке по названию и модели

        :param list_eq: список техники
        :param name_ey: проверяемое название техники
        :param model_eq: проверяемое название модели
        :return: int: индекс - если найдено соответствие / -1 - если соответствий нет
        """
        list_eq = [(el.name, el.model) for el in list_eq]
        if (name_ey, model_eq) in list_eq:
            idx = list_eq.index((name_ey, model_eq))
            return idx
        return -1

    def __add_printer(self) -> None:
        """
        Добавление нового принтера на склад или обновление
        количества уже имеющихся

        :return: None
        """
        tmp = {
            'model': input('Введите модель принтера: '),
            'number': Ui.pos_number(int, 'Введите количество позиций: '),
        }
        idx = self.__is_on_list(self.equipments, 'Принтер', tmp['model'])
        if idx != -1:
            print('Внимание: данная модель уже имеется на складе.\n'
                  '(Обновляем количество данной модели)')
            self.equipments[idx].number += tmp['number']
        else:
            tmp['color'] = input('Цветной/черно-белый: ')
            tmp['com_interface'] = input('Интерфейс подключения: ')
            tmp = Printer(**tmp)
            self.equipments.append(tmp)

    def __add_scanner(self) -> None:
        """
        Добавление нового сканера на склад или обновление
        количества уже имеющихся

        :return: None
        """
        tmp = {
            'model': input('Введите модель сканера: '),
            'number': Ui.pos_number(int, 'Введите количество позиций: '),
        }
        idx = self.__is_on_list(self.equipments, 'Сканер', tmp['model'])
        if idx != -1:
            print('Внимание: данная модель уже имеется на складе.\n'
                  '(Обновляем количество данной модели)')
            self.equipments[idx].number += tmp['number']
        else:
            tmp['max_dpi'] = input('Макс. разрешение: ')
            tmp['speed'] = Ui.pos_number(int, 'Скорость сканирования: ')
            tmp = Scanner(**tmp)
            self.equipments.append(tmp)

    def __add_xerox(self) -> None:
        """
        Добавление нового МФУ на склад или обновление
        количества уже имеющихся

        :return: None
        """
        tmp = {
            'model': input('Введите модель МФУ: '),
            'number': Ui.pos_number(int, 'Введите количество позиций: '),
        }
        idx = self.__is_on_list(self.equipments, 'МФУ', tmp['model'])
        if idx != -1:
            print('Внимание: данная модель уже имеется на складе.\n'
                  '(Обновляем количество данной модели)')
            self.equipments[idx].number += tmp['number']
        else:
            tmp['color'] = input('Цветной/черно-белый: ')
            tmp['functions'] = input('Функции МФУ: ')
            tmp = Xerox(**tmp)
            self.equipments.append(tmp)

    def __add_dep(self) -> None:
        """
        Добавление нового подразделения

        :return: None
        """
        name = input('Введите название подразделения:\n>>>')
        if name not in self.office:
            self.office[name] = list()
        else:
            print('Ошибка: подразделение с таким именем уже существует')

    def add(self, type_yq='') -> None:
        """
        Добавить новый элемент на склад

        :param type_yq: тип добавляемого элемента
                        ('', '-p', '-s', '-x', '-d')
        :return: None
        """
        if type_yq == '-d':
            self.__add_dep()
        elif type_yq == '-p':
            self.__add_printer()
        elif type_yq == '-s':
            self.__add_scanner()
        elif type_yq == '-x':
            self.__add_xerox()

    def show_dep(self, name_dep='') -> None:
        """
        Показать все подразделения или технику отдельного подразделения

        :param name_dep: название подразделения которое необходимо вывести на экран
                        (если не указано функция выведет названия всех подразделений)
        :return: None
        """
        if name_dep == '':
            print('Все подразделения компании:')
            for idx, key in enumerate(self.office, 1):
                print(f'{idx:^5}: {key:^10}')
        else:
            print(f'За подразделением "{name_dep}" числится следующее оборудование:')
            for idx, el in enumerate(self.office[name_dep], 1):
                print(f'{idx:^5}: {el.name:^10} {el.model:^10} ({el.number} шт.)')

    def give_take_eq(self, name_dep: str,
                     idx_eq: int, num_eq: int,
                     give_take: bool) -> None:
        """
        Передача техники в подразделения

        :param name_dep: название подразделения
        :param idx_eq: индекс передаваемой техники
        :param num_eq: количество передаваемой техники
        :param give_take: True - выдать технику со склада (по умолчанию),
                          False - вернуть технику на склада
        :return: None
        """
        list1, list2 = [], []
        if give_take:
            list1, list2 = self.equipments, self.office[name_dep]
        else:
            list2, list1 = self.equipments, self.office[name_dep]

        tmp = copy(list1[idx_eq])
        tmp.number = num_eq
        list1[idx_eq].number -= num_eq
        if list1[idx_eq].number == 0:
            del list1[idx_eq]

        idx_eq = self.__is_on_list(list2, tmp.name, tmp.model)
        if idx_eq != -1:
            list2[idx_eq].number += num_eq
        else:
            list2.append(tmp)

    def __str__(self):
        tmp_str = f'За подразделением "{self.name}" числится следующее оборудование:\n'
        for idx, el in enumerate(self.equipments, 1):
            tmp_str += f'{idx:^5}: {el.name:^10} {el.model:^10} ({el.number} шт.)\n'
        return tmp_str[0:-1]


class Equipment(ABC):
    @abstractmethod
    def __init__(self, name, model, number):
        self.name = name
        self.model = model
        self.number = number

    @abstractmethod
    def get_dict(self) -> dict:
        pass

    def __str__(self):
        content = ''
        tmp = self.get_dict()
        for key, value in tmp.items():
            content += f'{key:^10} : {value}\n'
        return content[0: -1]


class Printer(Equipment):
    def __init__(self, model, color, com_interface, number):
        super().__init__('Принтер', model, number)
        self.color = color
        self.com_interface = com_interface

    def get_dict(self) -> dict:
        tmp = {
            'Название': self.name,
            'Модель': self.model,
            'Количество позиций': self.number,
            'Цвет печати': self.color,
            'Интерфейс подключения': self.com_interface,
        }
        return tmp


class Scanner(Equipment):
    def __init__(self, model, max_dpi, speed, number):
        super().__init__('Сканер', model, number)
        self.max_dpi = max_dpi
        self.speed = speed

    def get_dict(self):
        return {
            'Название': self.name,
            'Модель': self.model,
            'Макс. разрешение': self.max_dpi,
            'Скорость сканирования': self.speed,
        }


class Xerox(Equipment):
    def __init__(self, model, functions, color, number):
        super().__init__('МФУ', model, number)
        self.functions = functions
        self.color = color

    def get_dict(self):
        return {
            'Название': self.name,
            'Модель': self.model,
            'Цвет печати': self.color,
            'Функции МФУ': self.functions,
        }


commands = {
    'help': Ui.help,
    'add': Ui.add,
    'exit': Ui.exit_app,
    'cd': Ui.cd,
    'show_dep': Ui.show_dep,
    'show_st': Ui.show_st,
}


st = Storage("Cклад")
st = Ui.help(st)
while True:
    user_answer = input('>>>').strip()
    command = user_answer.split()[0]
    param = user_answer.replace(command, '').strip()
    try:
        func = commands[command]
        st = func(st, param)
        print()
    except KeyError:
        print(f'Ошибка: неизвестная команда "{command}"\n')
