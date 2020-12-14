# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def print_info(**kwargs):
    result = ""
    for key in kwargs:
        result += f"{key}: {kwargs[key]}; "
    print(result)


dict_user = {
    "name": "Петр",
    "surname": "Петров",
    "year": "1992",
    "city": "Рязань",
    "email": "petya@mail.ru",
    "phone": "89998887575"
}

print_info(name="Иван", surname="Бублик", year="1997", city="Москва", email="vanya@mail.ru", phone="89998887676")
print_info(**dict_user)

