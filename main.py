# import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt


def array_random_numbers() -> list:
    return [int(input('Введите значение a - ')), int(input('Введите значение b - '))]


n = int(input('Введите значение n - '))
a, b = array_random_numbers()
while a >= b:
    print('ERROR!\n\nПовторите ввод чисел a, b\n\nЧисло a не должно превышать число b!\n')
    a, b = array_random_numbers()

# n = 5
# a = -60
# b = 60

arr = np.random.randint(low=min(a, b), high=max(a, b), size=(n, n))

print(arr)
