import os
from user import User
from field import Field

# temp = input("Пожалуйста, введите ваше имя:\n>>>")
# player = User(temp)

play_field = Field()

# player.print_info()
play_field.print_field()

while True:
    user_answer = input()
    if ("d", "D", "в", "В").count(user_answer):
        play_field.move_right()
        play_field.add_rand_value()
        play_field.print_field()
    elif ("a", "A", "ф", "Ф").count(user_answer):
        play_field.move_left()
        play_field.add_rand_value()
        play_field.print_field()


