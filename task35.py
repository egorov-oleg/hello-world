x=int(input('Введите натуральное число: '))
n=int(input('Введите основание системы счисления: '))
r=0
z=1
while x!=0:
    r=r+z*(x%n)
    x=x//n
    z=z*10
print(r)
