#1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
#Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
import cProfile,time
def main():
    begin = time.perf_counter()
    number = input('Введите трёхзначное число: ')

    sum_ = 0
    prod_ = 1
    if int(number) < 100 or int(number) > 999:

         print ('Вы ввели неправельное число')
    else:
        for i in number:
            sum_ += int(i)
            prod_ *= int(i)
        print(f"Сумма цифр числа {number}: {sum_}")
        print(f"Произведение цифр: {number}: {prod_}")
        end = time.perf_counter()
        print('Выполнено за:',end - begin)
cProfile.run('main()')
def main2():
    begin = time.perf_counter()
    number = int(input('Введите трёхзначное число: '))
    number1 = number // 100
    number2 = (number // 10) % 10
    number3 = number % 10
    sum_ = number1 + number2 + number3
    prod_ = number1 * number2 * number3
    print(f"Сумма цифр числа {number}: {sum_}")
    print(f"Произведение цифр: {number}: {prod_}")
    end = time.perf_counter()
    print('Выполнено за:',end - begin)
cProfile.run('main2()')
# Сравнил 1 задачу первого урока в двук вариантах библиотекой тайм и библиотекой профайл. второй вариант написание
# программы оказался быстрей.