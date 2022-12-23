# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""Doc."""
import random
import os
os.system('cls')


def get_list(n):  # функция рандомного заполнения списка
    lst = []
    for _ in range(n):
        lst.append(random.randrange(0, n))
    return lst


n = int(input('Enter the size of the list: '))
lst = get_list(n)
print(lst)
print(f'On odd positions elements: {lst[1::2]}')
print(f'Answer: {sum(lst[1::2])}')
