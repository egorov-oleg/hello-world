a=int(input('Введите четырехзначное число \n'))
b=a%100
a=a//100
c=b%10
b=b//10
c=c*10+b
if a==c:
    print('Данное число является палиндромом')
else:
    print('Данное число не является палиндромом')
