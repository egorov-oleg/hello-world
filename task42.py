a=int(input('Введите последовательность чисел:\n'))
count1=0
while a!=0:
    count=0
    b=1
    while a>=b:
        if a%b==0:
            count=count+1
            b=b+1
        else:
            b=b+1
    if count==2:
        count1=count1+1
    a=int(input())
print('Простых чисел в последовательности:',count1)
