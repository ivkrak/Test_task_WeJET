from functions import *

if __name__ == "__main__":
    n = int(input('Введите значение n(размер стороны массива) - '))
    a, b = array_random_numbers()
    while a >= b:
        print('ERROR!\n\nПовторите ввод чисел a, b\n\nЧисло a не должно превышать число b!\n')
        a, b = array_random_numbers()
    arr = random_array(low=a, high=b, size=n)

    print(f'Сгенерированный массив:\n {str_array(arr)}')

    print(sum_of_numbers_in_a_triangle(arr))
