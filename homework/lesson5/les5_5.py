# 5. Создать (программно) текстовый файл, записать в него программно
# набор чисел, разделенных пробелами. Программа должна подсчитывать
# сумму чисел в файле и выводить ее на экран.

from random import randint

content = ''
for _ in range(20):
    content += str(randint(0, 100)) + ' '
with open(r'example\text5_5.txt', 'w') as new_file:
    new_file.write(content)

with open(r'example\text5_5.txt') as new_file:
    content = new_file.read()
    result = sum([int(el) for el in content.split()])

print(content)
print(result)
