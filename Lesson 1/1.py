#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
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


