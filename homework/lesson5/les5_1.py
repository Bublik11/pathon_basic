# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.


msgs = []
while True:
    line = input("Добавление строки (для завершения работы "
                 "программы введите пустую строку):\n>>>")
    if line == '':
        break
    else:
        line += '\n'
        msgs.append(line)

with open(r'example\text5_1.txt', 'w') as new_file:
    new_file.writelines(msgs)
