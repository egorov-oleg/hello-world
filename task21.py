a=int(input('Введите 2 натуральных числа: \n'))
b=int(input())
c=1
summa=0
summa1=0
while a>c:
    if a%c==0:
        summa=summa+c
    c=c+1
if summa==b:
    c=1
    while b>c:
        if b%c==0:
            summa1=summa1+c
        c=c+1
    if summa1==a:
        print('Данные числа являются дружественными')
    else:
        print('Данные числа не являются дружественными')
else:
    print('Данные числа не являются дружественными')
