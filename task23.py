a=int(input('Введите 2 натуральных числа: \n'))
b=int(input())
prod=a*b
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
b=prod//a
print('Наименьшее общее кратное данных чисел:',b)
