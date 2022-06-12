#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

n = [random.randint(0, 99) for _ in range(10)]
print(f'Массив до изменения: {n}')

max_ = n[0]
min_ = n[0]

for i in n:
    if i > max_:
        max_ = i
    elif i < min_:
        min_ = i
min_array = n.index(min_)
max_array = n.index(max_)
n[min_array], n[max_array] = n[max_array], n[min_array]
print(f'Максимальный элемент массива: {max_}\nМинимальный элемент массива: {min_}\nМассив после эзменения:{n}')