n=int(input('Введите n: '))
k=int(input('Введите k так, чтобы было k<n: '))
num=1
i=n
while i>=n-k+1:
    num=num*i
    i=i-1
denom=1
i=1
while i<=k:
    denom=denom*i
    i=i+1
print(num//denom)
