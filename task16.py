a=int(input('Введите натуральное число: '))
count=0
b=1
while a-b>-1:
    if a%b==0:
        count=count+1
        b=b+1
    else:
        b=b+1
print('Количество делителей у данного числа:',count)
