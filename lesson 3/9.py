#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random
lines = 10
column = 5
array = []
for i in range(column):
    array2 = []
    for j in range(lines):
        n = int(random()*200)
        array2.append(n)
        print('%4d' % n,end='')
    array.append(array2)
    print()

max_ = -1
for j in range(lines):
    min_ = 200
    for i in range(column):
        if array[i][j] < min_:
            min_ = array[i][j]
    if min_ > max_:
        max_ = min_
print("Максимальный элемент среди минимальных: ", max_)