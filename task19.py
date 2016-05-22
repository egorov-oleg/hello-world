a=int(input('Введите количество первых простых чисел: '))
b=0
count=0
count1=0
while count1<a:
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
        count1=count1+1
