a=int(input('Введите члены последовательности:\n'))
if a!=0:
    b=int(input())
else:
    print('Последовательность не монотонна')
    raise SystemExit
delta=a-b
while b!=0:
    if delta*(a-b)<=0:
        print('Последовательность не монотонна')
        break
    a=b
    b=int(input())
if b==0:
    print('Последовательность монотонна')
