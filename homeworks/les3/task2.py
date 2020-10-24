"""
 Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""

def person(**kwargs):
    return kwargs

# print(person(name = "John", surname = "Smith", year_of_birth = 1975, location = 'Springfild',
#              email = 'JSmith@gmail.com', number = 581735812548))

# print(person('name'))
person1 = person(name = "John", surname = "Smith", year_of_birth = 1975, location = 'Springfild',
             email = 'JSmith@gmail.com', number = 581735812548)
for key, value in person1.items():
    print(f'{value}', end=" ")
