year=int(input('Введите год: '))
if (year % 4 or year % 400 == 0 ) and year % 100 !=0:
    print("Нет")
else:
    print("Да")