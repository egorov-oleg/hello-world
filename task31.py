n=int(input('Введите натуральное число: '))
r=0
while n!=0:
    r=r*10
    r=r+n%10
    n=n//10
print(r)
