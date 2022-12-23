# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
"""Doc."""
import random
import os
os.system('cls')


def get_list(n):  # функция рандомного заполнения списка
    lst1 = []
    for _ in range(n):
        lst1.append(random.randrange(0, n))
    return lst1


def multiplying_lists(lst1, n):
    lst2 = []
    for i in range(len(lst1)):
        while i < len(lst1)/2 and n > len(lst1)/2:
            n = n - 1
            a = lst1[i] * lst1[n]
            lst2.append(a)
            i += 1
    return lst2


n = int(input('Enter the size of the list: '))
lst1 = get_list(n)
print(f'List 1: {lst1}')
lst2 = multiplying_lists(lst1, n)
print(f'List 2: {lst2}')
