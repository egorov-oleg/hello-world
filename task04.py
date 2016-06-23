c=int(input('Введите число \n'))
a=c%10
c=c//10
b=c%10
c=c//10
c=a*100+b*10+c
print(c)