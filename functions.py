import numpy as np


def array_random_numbers():
    """
    **Принимает на вход значения для случайной генерации чисел**

        * a - Минимальное значение числа в массиве
        * b - Максимальное значение числа в массиве
    **Возвращает список из двух значений [a, b]**
    """
    return [int(input('Введите значение a(минимальное значение сгенерированного числа) - ')),
            int(input('Введите значение b(максимальное значение сгенерированного числа) - '))]


def random_array(low, high, size):
    """
    **Создаёт массив типа numpyArray**

    * low - Минимальное значение случайного числа
    * high - Максимальное значение случайного числа
    * size - Размер матрицы AxA
    """
    return np.random.randint(low=low, high=high, size=(size, size))


def str_array(arr):
    """
    **Красиво выводит двумерный массив**

    * Принимает на вход массив numpyArray
    """
    string_arr = str(arr)[1:-1].replace('[', '|')
    string_arr = string_arr.replace(']', '|')
    return string_arr


def sum_of_first_triangle(arr):
    triangle_1 = []
    shape = arr.shape[0]
    a = 0
    b = int(shape)
    for j in range(int(shape / 2) if shape % 2 == 0 else int(shape / 2) + 1):
        for i in range(a, b):
            triangle_1.append(arr[j][i])
            # print(arr[j][i])
        a += 1
        b -= 1
    return sum(triangle_1)


def sum_of_third_triangle(arr):
    arr = arr.transpose()
    return sum_of_first_triangle(arr)


def sum_of_fourth_triangle(arr):
    arr = arr.transpose()
    return sum_of_second_triangle(arr)


def sum_of_second_triangle(arr):
    triangle_2 = []
    shape = arr.shape[0]
    if shape % 2 == 0:
        b = int(shape / 2) + 1
        a = int(shape / 2) - 1
        x = int(shape / 2)
    else:
        b = int(shape / 2) + 1
        a = int(shape / 2)
        x = int(shape / 2)

    for j in range(x, shape):
        for i in range(a, b):
            triangle_2.append(arr[j][i])
        a -= 1
        b += 1
    return sum(triangle_2)


def sum_of_numbers_in_a_triangle(arr):
    """
    **Выводит суммы треугольников**

    * принимает на вход массив numpyArray
    * выводит список с суммами треугольников -> [сумма I △, сумма II △, сумма III △, сумма IV △]
    """
    out = f'Первый треугольник: {sum_of_first_triangle(arr)}\n' \
          + f'Второй треугольник: {sum_of_second_triangle(arr)}\n' \
          + f'Третий треугольник: {sum_of_third_triangle(arr)}\n' \
          + f'Четвертый треугольник: {sum_of_fourth_triangle(arr)}'
    return out
