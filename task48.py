n=int(input('Введите n: '))
fib0=0
fib1=1
print(fib0)
i=2
if n!=0:
    while i<=n:
        fib=fib1+fib0
        print(fib)
        fib0=fib1
        fib1=fib
        i=i+1
