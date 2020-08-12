"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def test():
    revers(12345678912345678912345678912345678911111111111111)
    revers_2(12345678912345678912345678912345678911111111111111)
    revers_3(12345678912345678912345678912345678911111111111111)


cProfile.run('test()')

print(
    timeit(
        'revers(12345678912345678912345678912345678911111111111111)',
        setup='from __main__ import revers',
        number=100000))
print(
    timeit(
        'revers_2(12345678912345678912345678912345678911111111111111)',
        setup='from __main__ import revers_2',
        number=100000))
print(
    timeit(
        'revers_3(12345678912345678912345678912345678911111111111111)',
        setup='from __main__ import revers_3',
        number=100000))

'''в данных примерах использование cProfile не дает должной аналитики - мы только увидели, что
рекурсия вызывалась 57 раз за вызов, так как цифры слишком малы,
эффективнее использовать timeit, тк есть возможность исполнения нашего кода сотню тысяч раз,
что дает представление о том, что использование самым эффективным алгоритмом является использование
встроенной функции обратного среза, менее эффективным средством является использование цикла,
и самым затратным по времени - рекурсия'''
