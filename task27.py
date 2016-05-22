x=int(input('Введите x: '))
n=int(input('Введите степень многочлена: '))
res=0
i=1
print('Введите коэффициент a:')
while i<=n+1:
    a=int(input())
    res=res*x+a
    i=i+1
print('Значение многочлена равно', round(res, 3))
