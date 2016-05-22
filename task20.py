a=int(input('Введите натуральное число: '))
b=1
summa=0
while a>b:
    if a%b==0:
        summa=summa+b
    b=b+1
if summa==a:
    print('Данное число является совершенным')
else:
    print('Данное число не является совершенным')
