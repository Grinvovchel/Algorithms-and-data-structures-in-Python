#7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.
import random

n = [random.randint(0, 99) for _ in range(10)]
print(n)

min1 = 0
min2 = 1

for i in n:
    if n[min1] > i:
        min2 = min1
        min1 = n.index(i)
    elif n[min2] > i:
        min2 = n.index(i)

print(f'Два наименьших элемента массива : {n[min1]}  {n[min2]}')