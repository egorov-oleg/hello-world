n=int(input('Введите n: '))
fib0=0
fib1=1
i=2
while i<=n:
    fib=fib1+fib0
    fib0=fib1
    fib1=fib
    i=i+1
if n==0:
    fib1=0
print(fib1)
