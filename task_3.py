"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from collections import deque
from timeit import timeit
one = [i for i in range(20)]
my_deque_l = deque(one)
two = [i for i in range(20)]
my_deque_r = deque(one)


def deque_fill_left():
    for i in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        my_deque_l.appendleft(i)
    return my_deque_l


def deque_fill_right():
    for i in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        my_deque_r.append(i)
    return my_deque_r


def list_fill():
    for i in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        two.append(i)
    return two


print(f"Заполнение дека слева: {timeit('deque_fill_left()', setup='from __main__ import deque_fill_left')}")
print(f"Заполнение дека справа: {timeit('deque_fill_right()', setup='from __main__ import deque_fill_right')}")
print(f"Заполнение списка: {timeit('list_fill()', setup='from __main__ import list_fill')}")

"""Дек заплняется на порядок быстрее списка, и не важно с какой стороный производить его заполнение"""
