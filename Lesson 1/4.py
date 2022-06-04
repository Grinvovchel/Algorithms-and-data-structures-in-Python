# 4. Написать программу, которая генерирует в указанных пользователем границах
import random

Number1 = int(input('Введите первое число '))
Number2 = int(input('Введите второе число '))

# случайное целое число;

if Number1 >= Number2:
    print('Первое число не может быть больше либо равно второму числу')
else:
    print(f'Случайное число из выбранного вами диапазона = {random.randint(Number1, Number2)}')

# случайное вещественное число;

Number1 = float(Number1)
Number2 = float(Number2)
num = random.uniform(Number1, Number2)

print(f"Случайное вещественное число из выбранного вами диапазона = {format(num, '.3f')}")

# случайный символ.

let1 = input('Введите первую букву диапазона (английские, нижний регистр)\n')
let2 = input('Введите вторую букву диапазона (английские, нижний регистр)\n')

alph = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

let1_ind = alph.index(let1)
let2_ind = alph.index(let2)

rand_let = alph[random.randint(let1_ind, let2_ind)]

print(f'Случайная буква из выбранного вами дипазона - "{rand_let}"')