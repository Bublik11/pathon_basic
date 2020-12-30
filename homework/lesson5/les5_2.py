# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


with open(r'example\text5_2.txt') as new_file:
    content = new_file.readlines()
    msgs = [len(line.strip().split(' ')) for line in content]
    for idx, el in enumerate(msgs, 1):
        print(f"{idx} строка: {el} слов")
