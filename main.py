from functions import *

# n = int(input('Введите значение n - '))
# a, b = array_random_numbers()
# while a >= b:
#     print('ERROR!\n\nПовторите ввод чисел a, b\n\nЧисло a не должно превышать число b!\n')
#     a, b = array_random_numbers()

# Проверочные данные
# n = 5
# a = -60
# b = 60

# arr = random_array(low=min(a, b), high=max(a, b), size=n)

arr = np.array([[56, 43, 45, 45, 34],
        [-56, 45, -6, 5, 6],
        [5, -6, 4, 6, 6],
        [45, 6, -8, 5, 1],
        [0, 7, 8, 5, 7]])

print_array(arr)

shape = arr.shape[0]
print(f'shape: {shape}')
a, b = 0, shape
for j in range(3):
    print(f'j: {j}')
    for i in range(a, b):
        print('__________________')
        print(arr[::][i])
        a += 1
        b -= 1

