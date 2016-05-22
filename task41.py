n=int(input('Введите натуральное число n: '))
a=int(input('Введите члены последовательности: \n'))
prod=1
while a!=0:
    if a>9 and a<100 and a%n==0:
        prod=prod*a
    a=int(input())
if prod!=1:
    print('Произведение двузначных членов, делящихся на n, равно:',prod)
else:
    print('Нет двузначных элементов, делящихся на n')
