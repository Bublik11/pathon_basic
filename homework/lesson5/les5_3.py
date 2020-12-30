# 3. Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников имеет
# оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.

temp_person = {
    "surname": '',
    "salary": 0
}

persons = []
with open(r'example\text5_3.txt') as f_data:
    content = f_data.readlines()
    for line in content:
        temp_person["surname"] = line.split(' ')[0]
        temp_person["salary"] = float(line.split(' ')[1])
        print(temp_person["surname"], ' ', temp_person["salary"])
        persons.append(temp_person.copy())

print()
low_salary = [el['surname'] for el in persons if el['salary'] < 20000]
middle_salary = sum([el['salary'] for el in persons]) / len(persons)
print("Сотрудники, у которых зарплата меньше 20 тыс.:")
for ind, el in enumerate(low_salary, 1):
    print(f"{ind}. {el}")
print("")
print(f"Средняя зарплата всех сотрудников: {middle_salary}")
