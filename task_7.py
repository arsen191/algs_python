"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
input_num = int(input('Введите число для создания множества от 0 до n: '))
gen_list = [el for el in range(1, input_num + 1)]


def my_func(lst):
    global sum_list
    if len(lst) == 0:
        sum_list.reverse()
        return print(f'Результат вычислений 1+2+...+n для множества: {sum_list}')
    else:
        return sum_list.append(sum(lst)), my_func(lst[:-1])


def my_func1(lst):
    global my_list
    if len(lst) == 0:
        return print(f'Результат вычислений n(n+1)/2 для множества: {my_list}')
    else:
        return my_list.append(
            int(lst[0] * (lst[0] + 1) / 2)), my_func1(lst[1:])


my_list = []
sum_list = []
a = my_func(gen_list)
b = my_func1(gen_list)
print(a == b)
