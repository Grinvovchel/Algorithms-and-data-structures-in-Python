#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

n = [random.randint(0, 99) for _ in range(10)]
print(f'Массив: {n}')

min_ = 0
max_ = 0
step = 1
sum_ = 0

for i in n:
    if n[min_] > i:
        min_ = n.index(i)
    elif n[max_] < i:
        max_ = n.index(i)

if max_ - min_ < 0:
    step = -1

for i in n[min_ + step:max_:step]:
    sum_ += i


print(f'Между элементами:{n[min_]}   {n[max_]}\nСумма элементов: {sum_}')