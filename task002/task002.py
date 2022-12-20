# 2. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.
"""Doc."""
import itertools
from random import randint
import os
os.system('cls')

n = 7

mylist = ['jh', 'sdhfogf', 'kjahsd', '24', 'dpo', '7']


def find_number(n, lst):
    return str(n) in lst


print(find_number(n, mylist))


def get_list(raw, col, frst, last):  # функция формирование перемешанного
    # списка
    return [[randint(frst, last) for _ in range(col)] for _ in range(raw)]


def find_number(n, mylist):  # функция Нахождение числа во вложенном списке
    return n in list(itertools.chain(*mylist))


raw = 3
col = 3
frst = 1
last = 100
mylist = get_list(raw, col, frst, last)

print(mylist)
n = int(input(('Return number: ')))
print(find_number(n, mylist))
