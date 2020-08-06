"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import sys
import time

sys.setrecursionlimit(10000)
my_list = []
my_dict = {}


def fill_list(n, lst):
    if n == 1000:
        return lst
    else:
        return lst.append(n), fill_list(n + 1, lst)


def fill_dict(n, dictionary):
    if n == 1000:
        return dictionary
    else:
        return dictionary.setdefault(n), fill_dict(n + 1, dictionary)


list_start = time.time()
fill_list(1, my_list)
list_fin = time.time()
print(f'Время заполнения списка: {round(list_fin - list_start, 4)}')

dict_start = time.time()
fill_dict(1, my_dict)
dict_fin = time.time()
print(f'Время заполнения словаря: {round(dict_fin - dict_start, 4)}')
