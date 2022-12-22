N=int(input())

Dane=[]
for ind in range(N):
    Wejscie = input().split()
    K=len(Wejscie)
    Dane.append(Wejscie)

Osoby=[]
Zawody=[]

for g in range(len(Dane)):
    Osoby.append(Dane[g][0:2])
    
    Zawody.append(Dane[g][2:K])

print(Osoby,Zawody)