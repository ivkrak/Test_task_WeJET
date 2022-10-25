# import pandas as pd
import numpy as np


# import matplotlib.pyplot as plt


def array_random_numbers():
    """
    **Принимает на вход значения для случайной генерации чисел**

        * a - Минимальное значение числа в массиве
        * b - Максимальное значение числа в массиве
    **Возвращает список из двух значений [a, b]**
    """
    return [int(input('Введите значение a - ')), int(input('Введите значение b - '))]


def print_array(arr):
    """
    **Красиво выводит двумерный массив**

    * Принимает на вход массив numpyArray
    """
    for i in arr:
        print(str(i)[1:-1])


def sum_of_numbers_in_a_triangle(arr):
    """
    **Выводит суммы треугольников**

    * принимает на вход массив np.array
    * выводит список с суммами треугольников -> [сумма I △, сумма II △, сумма III △, сумма IV △]
    """
    pass


n = int(input('Введите значение n - '))
a, b = array_random_numbers()
while a >= b:
    print('ERROR!\n\nПовторите ввод чисел a, b\n\nЧисло a не должно превышать число b!\n')
    a, b = array_random_numbers()


# Проверочные данные
# n = 5
# a = -60
# b = 60

arr = np.random.randint(low=min(a, b), high=max(a, b), size=(n, n))

print_array(arr)