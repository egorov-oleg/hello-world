a=int(input('Введите натуральное число: '))
count=0
b=1
while a>=b:
    if a%b==0:
        count=count+1
        b=b+1
    else:
        b=b+1
if count==2:
    print('Данное число является простым')
else:
    print('Данное число не является простым')
