import math
n=int(input('Введите n, чтобы обозначить область значений a [1; n] \n'))
a=1
while a<=n:
    x1=round(math.sqrt(a*a+3)-a, 3)
    x2=round(-math.sqrt(a*a+3)-a, 3)
    print('a='+str(a), 'x1='+str(x1), 'x2='+str(x2))
    a=a+1
    
