"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""
from collections import Counter, deque


def build_tree(word):
    tmp = Counter(word)
    my_tree = deque(sorted(tmp.items(), key=lambda x: x[1]))
    if len(my_tree) != 1:
        while len(my_tree) > 2:
            m = my_tree[0][1] + my_tree[1][1]
            cut_el = ({0: my_tree.popleft()[0],
                       1: my_tree.popleft()[0]}, m)
            for idx, el in enumerate(my_tree):
                if m > el[1]:
                    if idx == len(my_tree) - 1:
                        my_tree.append(cut_el)
                        break
                    else:
                        continue
                else:
                    my_tree.insert(idx, cut_el)
                    break
        else:
            m = my_tree[0][1] + my_tree[1][1]
            cut_el = ({0: my_tree.popleft()[0],
                       1: my_tree.popleft()[0]}, m)
            my_tree.append(cut_el)
            return my_tree[0][0]
    else:
        cut_el = ({0: my_tree.popleft()[0], 1: None})
        my_tree.append(cut_el)
        return my_tree[0]


code_table = dict()


def haffman(tree, path=''):
    if type(tree) != dict:
        code_table[tree] = path
    else:
        haffman(tree[0], path=f'{path}0')
        haffman(tree[1], path=f'{path}1')


s = 'Beep boop beer!'.lower()

haffman(build_tree(s))
print(code_table)
for v in code_table.values():
    print(f'{v}', end=' ')
