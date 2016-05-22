n=int(input('Введите n: '))
fib0=0
fib1=1
i=2
summa=0
while i<=n:
    fib=fib1+fib0
    summa=summa+fib
    fib0=fib1
    fib1=fib
    i=i+1
print(summa)
