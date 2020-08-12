"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
import timeit


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


@memorize
def recursive_reverse_mem(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print(
    timeit.timeit(
        'recursive_reverse(123456789)',
        setup='from __main__ import recursive_reverse',
        number=100000))
"""добавил мемоизацию, по результатам видим заметную оптимизацию по времени"""
print(
    timeit.timeit(
        'recursive_reverse_mem(123456789)',
        setup='from __main__ import recursive_reverse_mem',
        number=100000))
