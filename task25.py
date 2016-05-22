x=int(input('Введите число и его степень: \n'))
n=int(input())
r=1
while n!=1:
    if n%2!=0:
        r=r*x
    x=x*x
    n=n//2
print(x*r)
