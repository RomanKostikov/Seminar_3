# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
"""Doc."""
import os
os.system('cls')


def Fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


def NegaFibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2


def main():
    lst = [0]
    k = int(input('Enter number k: '))
    for i in range(1, k + 1):
        lst.append(Fibonacci(i))
        lst.insert(0, NegaFibonacci(i))
    print(lst)


if __name__ == "__main__":
    main()
