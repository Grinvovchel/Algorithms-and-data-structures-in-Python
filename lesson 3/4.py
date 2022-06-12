#4. Определить, какое число в массиве встречается чаще всего.
import random
n = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {n}')
max_array = 0
for i in n:
    if n.count(max_array) < n.count(i):
        max_array = n.index(i)
print(f'Число {n[max_array]}, встречается {n.count(max_array)} раза')