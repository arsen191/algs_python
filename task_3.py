"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
import hashlib
from uuid import uuid4

my_list = []
salt = uuid4().hex

S = input('Введите строку: ')
for i in range(0, len(S)):
    for j in range(len(S), 1, -1):
        if S[i:j] != '':
            hash_str = hashlib.sha256(salt.encode() + S[i:j].encode('utf-8')).hexdigest() + '/' + salt
            my_list.append(hash_str)

print(len(set(my_list)))
