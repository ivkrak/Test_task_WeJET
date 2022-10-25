import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# n = int(input('Введите значение n - '))
# a = int(input('Введите значение a - '))
# b = int(input('Введите значение b - '))

n = 5
a = -60
b = 60


arr = np.random.randint(low=min(a, b), high=max(a, b), size=(n, n))

print(arr)