c=int(input('Введите число \n'))
summ=0
while c!=0:
	rem=c%10
	c=c//10
	summ=summ*10+rem
	rem=0
print(summ)
