"""
Задание 2.
Предложить варианты оптимизации и доказать (наглядно, кодом) их эффективность
"""
from memory_profiler import profile


@profile
def func_1():
    new_arr = []
    nums = list(range(50000))
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    del nums
    return new_arr


func_1()
"""
Line #    Mem usage    Increment   Line Contents
================================================
     8     15.3 MiB     15.3 MiB   @profile
     9                             def func_1():
    10     15.3 MiB      0.0 MiB       new_arr = []
    11     17.2 MiB      1.9 MiB       nums = list(range(50000))
    12     18.3 MiB      0.0 MiB       for i in range(len(nums)):
    13     18.3 MiB      0.1 MiB           if nums[i] % 2 == 0:
    14     18.3 MiB      0.1 MiB               new_arr.append(i)
    15     16.5 MiB      0.0 MiB       del nums
    16     16.5 MiB      0.0 MiB       return new_arr
при удалении временного списка мы сэкономили немного памяти
Используется Python 3.8, разрядность ОС 64 бит
"""
