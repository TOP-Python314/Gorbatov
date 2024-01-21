num=int(input("Введите число: "))
three=num%10
two=num//100
one=num%10
print(f'Сумма цифр = {three + two + one}',f'Произведение цифр {one * two * three}',sep='\n')


"""
Введите число: 445
Сумма цифр = 14
Произведение цифр 100
"""