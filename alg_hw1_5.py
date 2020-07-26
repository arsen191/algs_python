"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""


class PlatesClass:
    def __init__(self):
        self.plates = [[], [], []]

    def push_in(self, plate):
        if len(self.plates[0]) < 10:
            self.plates[0].append(plate)
        elif len(self.plates[1]) < 10:
            self.plates[1].append(plate)
        elif len(self.plates[2]) < 10:
            self.plates[2].append(plate)

    def pop_out(self):
        for idx in range(2, -1, -1):
            if len(self.plates[idx]) != 0:
                return self.plates[idx].pop()
            else:
                continue

    def stack_size(self):
        return f'Количество тарелок в стопке 1: {len(self.plates[0])}\n' \
               f'Количество тарелок в стопке 2: {len(self.plates[1])}\n' \
               f'Количество тарелок в стопке 3: {len(self.plates[2])}'

    def full_stack(self):
        return f'Элементы стека 1: {self.plates[0]}\n' \
               f'Элементы стека 2: {self.plates[1]}\n' \
               f'Элементы стека 3: {self.plates[2]}'


if __name__ == '__main__':
    PlatesStack = PlatesClass()
    # наполняем стеки тарелками
    for i in range(0, 25):
        PlatesStack.push_in('Plate' + str(i))

    # проверяем размеры наших стеков
    print(PlatesStack.stack_size())
    # забираем одну тарелку
    print(PlatesStack.pop_out())
    # снова смотрим размеры наших стеков
    print(PlatesStack.stack_size())
    # смотрим наполнение наших стеков
    print(PlatesStack.full_stack())
