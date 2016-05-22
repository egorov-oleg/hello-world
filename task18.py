a=int(input('Введите натуральное число: '))
b=0
while a>=b:
    c=1
    count=0
    b=b+1
    while b>=c:
        if b%c==0:
            count=count+1
            c=c+1
        else:
            c=c+1
    if count==2:
        print(b)


