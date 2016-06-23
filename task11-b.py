n=int(input('Введите число \n'))
def binary(n):
        summ=0
        i=0
        while n!=0:
                rem=n%2
                n=n//2
                summ=summ*10+rem
                if summ==0:
                        i=i+1
        if i>0:
                summ=summ*10*i
        print(summ)
        return summ
def palynbin(summ):
        while summ%10==0:
                summ=summ//10
        a=summ
        digits=0
        while a!=0:
                a=a//10
                digits=digits+1
        i=1
        right=0
        while i<=digits//2:
                right=right*10+summ%10
                summ=summ//10
                i=i+1
        if digits%2==1:
                summ=summ//10
        if summ==right:
                print('Данное число является палиндромом')
        else:
                print('Данное число не является палиндромом')
palynbin(binary(n))
