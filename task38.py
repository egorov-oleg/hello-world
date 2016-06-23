n=int(input('Введите натуральное число: '))
a=n
digits=0
while a!=0:
    a=a//10
    digits=digits+1
i=1
right=0
while i<=digits//2:
    right=right*10+n%10
    n=n//10
    i=i+1
if digits%2==1:
    n=n//10
if n==right:
    print('Данное число является палиндромом')
else:
    print('Данное число не является палиндромом')
