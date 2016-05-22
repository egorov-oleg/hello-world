n=int(input('Введите натуральное число: '))
p=2
while n!=1:
    if n%p==0:
        print(p)
        n=n/p
    else:
        p=p+1
