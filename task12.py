import math
a=float(input('Для решения квадратного уравнения вида ax^2+bx+c введите a, b и c \n'))
b=float(input())
c=float(input())
D=b**2-4*a*c
if D>0:
    x1=(-b-math.sqrt(D))/2*a
    x2=(-b+math.sqrt(D))/2*a
    if float.is_integer(x1)==True:
        x1=int(x1)
    if float.is_integer(x2)==True:
        x2=int(x2)
    print('x1='+str(x1)+',', 'x2='+str(x2))
elif D==0:
    x1=-b/2*a
    if float.is_integer(x1)==True:
        x1=int(x1)
    print('x=',x1)
else:
    print('Уравнение корней не имеет')
