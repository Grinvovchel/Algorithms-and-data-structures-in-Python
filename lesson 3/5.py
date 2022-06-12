#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

n = [random.randint(-99, 99) for _ in range(10)]
print(f'Массив: {n}')

array_min = 0

for i in n:
    if n[array_min] > i:
        array_min = n.index(i)

if n[array_min] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'Минимальное значение: {n[array_min]}.\nПозиция минимального значения: {array_min}')