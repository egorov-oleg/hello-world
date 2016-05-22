a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
c=0
z=1
while a!=0:
    c=c+z*(b%10)
    z=z*10
    b=b//10
    c=c+z*(a%10)
    z=z*10
    a=a//10
print(c)
