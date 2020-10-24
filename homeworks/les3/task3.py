"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""
def my_func(num_1, num_2, num_3):
    if num_1 >= num_2 and num_2 >= num_3:
        return num_1 + num_2
    elif num_1 >= num_2 and num_2 <= num_3:
        return num_1 + num_3
    elif num_1 <= num_2 and num_1 <= num_3:
        return num_2 + num_3
    elif num_1 <= num_2 and num_1 >= num_3:
        return num_1 + num_2



num_1 = int(input('1-e число:'))
num_2 = int(input('2-e число:'))
num_3 = int(input('3-e число:'))

print(my_func(num_1, num_2, num_3))