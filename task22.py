a=int(input('Введите 2 натуральных числа: \n'))
b=int(input())
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print('Наибольгий общий делитель данных чисел:',a)
