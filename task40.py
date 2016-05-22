print('Введите последовательность натуральных чисел:')
a=int(input())
prod=1
while a!=0:
    if a%2==0:
        prod=prod*a
    a=int(input())
if prod!=1:
    print('Произведение четных членов последовательности равно', prod)
else:
    print('Нет четных членов')
