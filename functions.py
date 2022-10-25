import numpy as np


def array_random_numbers():
    """
    **Принимает на вход значения для случайной генерации чисел**

        * a - Минимальное значение числа в массиве
        * b - Максимальное значение числа в массиве
    **Возвращает список из двух значений [a, b]**
    """
    return [int(input('Введите значение a - ')), int(input('Введите значение b - '))]


def random_array(low, high, size):
    """
    **Создаёт массив типа numpyArray**

    * low - Минимальное значение случайного числа
    * high - Максимальное значение случайного числа
    * size - Размер матрицы AxA
    """
    return np.random.randint(low=low, high=high, size=(size, size))


def print_array(arr):
    """
    **Красиво выводит двумерный массив**

    * Принимает на вход массив numpyArray
    """
    print('\nМассив со случайными числами:\n')
    for i in arr:
        print(str(i)[1:-1])
    print('\n')


def sum_of_numbers_in_a_triangle(arr):
    """
    **Выводит суммы треугольников**

    * принимает на вход массив np.array
    * выводит список с суммами треугольников -> [сумма I △, сумма II △, сумма III △, сумма IV △]
    """
    pass