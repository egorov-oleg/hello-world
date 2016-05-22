first=1
last=0
a=int(input('Введите члены последовательности:\n'))
b=0
if a!=0:
    b=int(input())
while b!=0:
    last=a%10
    first=b
    while first>9:
        first=first//10
    if last!=first:
        print('last!=first')
        break
    a=b
    b=int(input())
if last==first:
    print('last=first')
