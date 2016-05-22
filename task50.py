x=int(input('Введите действительное число x: '))
eps=float(input('Введите точность esp: '))
expf=1
n=1
p=1
while abs(p)>=eps:
    p=p*x/n
    expf=expf+p
    n=n+1
print(expf)
