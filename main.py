from functions import *

if __name__ == "__main__":
    n = int(input('Введите значение n(размер стороны массива) - '))
    a, b = array_random_numbers()
    while a >= b:
        print('ERROR!\n\nПовторите ввод чисел a, b\n\nЧисло a не должно превышать число b!\n')
        a, b = array_random_numbers()
    arr = random_array(low = a, high = b, size = n)
    # Проверочные данные
    # n = 5
    # a = -60
    # b = 60
    #
    # arr = np.array([[56, 43, 45, 45, 34],
    #                 [-56, 45, -6, 5, 6],
    #                 [5, -6, 4, 6, 6],
    #                 [45, 6, -8, 5, 1],
    #                 [0, 7, 8, 5, 7]])

    print(f'Сгенерированный массив:\n {str_array(arr)}')

    print(sum_of_numbers_in_a_triangle(arr))
