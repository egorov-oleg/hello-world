n=int(input('Введите число \n'))
count=0
while n>0:
    count=count+n%2
    n=n//2
print('Количество единичных битов числа:', count)
