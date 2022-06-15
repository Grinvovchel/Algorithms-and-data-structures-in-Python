# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить
# в виде комментариев в файле с кодом.
import cProfile
n = int(input("n="))
def var1(): # Используя алгоритм «Решето Эратосфена»
    array = [i for i in range(n+1)]
    print(*array)
    array[1]=0
    i=2
    while i<= n/2:
        if array[i] !=0:
            j=i+i
            while j <=n:
                array[j]=0
                j=j+i
        i=i+1
    array=[i for i in array if array[i] !=0]
    print(*array)


def var2():#Без использования «Решета Эратосфена»
    array2=[]
    for i in range(2, n+1):
        k=0
        for j in range(1,i+1):
            if i % j == 0:
                k+=1
        if k==2:
            array2.append(i)
    print(*array2)
cProfile.run('var1()')
cProfile.run('var2()')
# С решетом Эратосвера код работает быстрее