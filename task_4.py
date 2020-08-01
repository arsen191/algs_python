"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

count_of_nums = int(input('Введите количество элементов: '))
el = 1
rez_list = [1]


def fill_rec(col):
    global el
    if col == 1:
        return rez_list
    else:
        el /= -2
        rez_list.append(el)
        return fill_rec(col - 1)


def sum_nums(cnt):
    if len(cnt) == 1:
        return cnt[0]
    else:
        return cnt[0] + sum_nums(cnt[1:])


print(sum_nums(fill_rec(count_of_nums)))
