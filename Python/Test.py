a=2

for i in range (10):
    a+=(a%(a-1))
    while a>=10:
        a-=9

print(a)