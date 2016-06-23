print('Введите 3 числа')
i=1
while i<=3:
    a=int(input())
    if i==2:
        b=a
    if i==3:
        c=a
    i=i+1
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
