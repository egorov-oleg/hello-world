n=int(input('Введите число символов: '))
if n==0:
    raise SystemExit
count=0
i=1
print('Введите круглые скобки через Enter')
while i<=n:
    c=input()
    if c=='(':
        count=count+1
    if c==')':
        count=count-1
    if count==-1:
        print('Баланс круглых скобок не соблюдён')
        raise SystemExit
    i=i+1
if count==0:
    print('Баланс круглых скобок соблюдён')
else:
    print('Баланс круглых скобок не соблюдён')
