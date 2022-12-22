wyraz="abcd"
rev=wyraz[::-1]

for i in range(len(wyraz)):
    print(wyraz[:i]+wyraz[i+1:])
    print(rev[:i]+rev[i+1: