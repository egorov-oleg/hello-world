n=int(input('Введите натуральное число: '))
digits=0
a=n
while a!=0:
    a=a//10
    digits=digits+1
left=0
right=0
i=1
while i<=digits//2:
    right=right+n%10
    n=n//10
    i=i+1
if digits%2==1:
    n=n//10
i=1
while i<=digits//2:
    left=left+n%10
    n=n//10
    i=i+1
if left==right:
    print('Данное число является счастливым билетом')
else:
    print('Данное число не является счастливым билетом')
