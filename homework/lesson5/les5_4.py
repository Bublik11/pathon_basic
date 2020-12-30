# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

temp_number = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


new_content = []
with open(r'example\text5_4.txt') as new_file:
    for line in new_file:
        temp_l = line.split(' - ')
        new_content.append(temp_number[temp_l[0].lower()].title() + ' - ' + temp_l[1])

with open(r'example\text5_4_new.txt', 'w') as new_file:
    new_file.writelines(new_content)
