from functions import *

n = int(input('Введите значение n - '))
a, b = array_random_numbers()
while a >= b:
    print('ERROR!\n\nПовторите ввод чисел a, b\n\nЧисло a не должно превышать число b!\n')
    a, b = array_random_numbers()

# Проверочные данные
# n = 5
# a = -60
# b = 60

arr = random_array(low=min(a, b), high=max(a, b), size=n )

print_array(arr)

sum_of_numbers_in_a_triangle()
