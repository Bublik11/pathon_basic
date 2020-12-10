# 6. * Реализовать структуру данных «Товары». Она должна представлять собой
# список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

list_product = []

dict_param = {
    "название": None,
    "цена": None,
    "количество": None,
    "ед": None
}

print("Список команд:\n"
      "-help - открывает список команд программы;\n"
      "-print - вывести все товары на экран;\n"
      "-stat - провести аналитику и вывести её на экран;\n"
      "-add - добавление нового товара;\n"
      "-exit - выход из программы.\n")

while True:
    command = input(">>>").lower()

    # команда "справка": показывает доступные команды
    if command == "-help":
        print("Список команд:\n"
              "-help - открывает список команд программы;\n"
              "-print - вывести все товары на экран;\n"
              "-stat - провести аналитику и вывести её на экран;\n"
              "-add - добавление нового товара;\n"
              "-exit - выход из программы.\n")

    # команда "добавить" - добавляет товар в список
    elif command == "-add":
        dict_param["название"] = input("Введите название товара:\n>>>").lower()

        while True:
            price = input("Введите цену товара:\n>>>")
            if price.isdigit():
                dict_param["цена"] = int(price)
                break
            else:
                print("Ошибка: введены неверные параметры.")

        while True:
            number = input("Введите количество товара:\n>>>")
            if number.isdigit():
                dict_param["количество"] = int(number)
                break
            else:
                print("Ошибка: введены неверные параметры.")

        dict_param["ед"] = input("Введите единицу измерения товара товара:\n>>>").lower()
        list_product.append((len(list_product), dict_param.copy()))
        print()

    # выводит все товары на экран
    elif command == "-print":
        if list_product is not None:
            for t in list_product:
                print(f"{t[0] + 1}\t{t[1]}")
            print()

    # собирает статистику по товарам и выводит на экран
    elif command == "-stat":
        if len(list_product):
            name, price, number, unit = [], [], [], set()
            for el in list_product:
                name.append(el[1].get("название"))
                price.append(el[1].get("цена"))
                number.append(el[1].get("количество"))
                unit.add(el[1].get("ед"))
            stat_dict = {
                "название": name,
                "цена": price,
                "количество": number,
                "ед": unit
            }
            print(stat_dict)
            print()
        else:
            print("Вы не ввели ни одного товара.\n")

    # выход из программы
    elif command == "-exit":
        break

    # ошибки ввода
    else:
        print("Ошибка: такой команды нет. "
              "Для вызова справки используйте команду \"-help\"\n")