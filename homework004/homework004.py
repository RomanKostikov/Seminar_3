# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
"""Doc."""
import os
os.system('cls')


def binary_number(n):
    s = ""
    while n != 0:
        s = str(n % 2) + s
        n //= 2
    return s


n = int(input("Enter number: "))
print(f'{n} => {binary_number(n)}')
