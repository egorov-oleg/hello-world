m=int(input('Введите 2 натуральных числа: \n'))
n=int(input())
if m>n:
    mini=n
else:
    mini=m
mindiv=0
i=2
while i<=mini:
    if n%i==0 and m%i==0:
        mindiv=i
        break
    else:
        i=i+1
if mindiv!=0:
    print('Наименьший нетривиальный делитель данных чисел:',mindiv)
else:
    print('Наименьшего нетривиального делителя нет')
