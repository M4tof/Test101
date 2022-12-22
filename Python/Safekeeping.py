D={'D':10,'Ei':1,'C':4,'Cc':8,'Uu':6,'A':4,'Aa':4}
D1=sorted(D.items(),key=lambda x:(-x[1],x[0]))

print(D1)
















#Stats ={"name":"","cpu":0,"gpu":0,"disc":0,"ram":0,"price":0}
n=int(input())
komputery=[]
for i in range(n):
    Dane=input().split()
    temp={"name":str(Dane[0]),"cpu":int(Dane[1]),"gpu":int(Dane[2]),"disc":int(Dane[3]),"ram":int(Dane[4]),"price":int(Dane[5])}
    komputery.append(temp)
    temp={}

m=int(input())
for i2 in range(m):
    wymogi = input().split()
    BranePodUwage = komputery[:]
    PrzeszlyTest=[]
    for i3 in range(len(wymogi)):
        requierment = wymogi[i3] #gpu:10 itd...
        requierment=requierment.split(':')
        for g in BranePodUwage:
            statystyka = g[requierment[0]]
            if statystyka >= int(requierment[1]):
                PrzeszlyTest.append(g)
    #print(PrzeszlyTest)
    if len(PrzeszlyTest)==1:
        print(PrzeszlyTest[0]["name"])








#max submatrix

N = input().split()
n,N = int(N[1]),int(N[0])

MAT=[]
for i1 in range(N):
    MAT.append(list(map(int,input().split())))

maks=0

def obrot(a): 
    mat2=[]
    for n in range(len(a[0])):
        temptab=[]
        for n2 in range(len(a)):
            temptab.append(a[n2][n])
        mat2.append(temptab)
    return mat2

def product(m): #m=mat
    y = len(m)
    rev = obrot(m)
    sumator=0
    for o in range(y):
        litesum=0
        for p in range(y):
            litesum = litesum + m[o][p]*rev[o][p]
        sumator=sumator+litesum
    return sumator

for i in range(N):
    for j in range(N):
        if i+n-1 <= N-1 and j+n-1 <=N-1:
            mat=[]
            for i2 in range(n):
                mat.append(MAT[i+i2][j:j+n])
            print(mat)
        print("------")


Butelki=[]
for ind in range(int(input())):
    A=input.split()
    Nazw=A[0]
    Zawartosc=int(A[1])+int(A[2])
    try:
        SdoW=int(A[1])/int(A[2])
    except:
        SdoW=int(A[1])
    Poj=int(A[3])
    Butelki.append([Nazw,Zawartosc,SdoW,Poj])
    #Nazwa,Ile litrów jest W,Stosunek Soku do H20,Maks pojemnosc

Butelki=sorted(Butelki)
for jnd in range(int(input())):
    F=input().split()
    From=F[0]
    To=F[1]
    IlePrzelać=From[1]%(To[3]-To[1])
    From[1]=From[1]-IlePrzelać
    if From[1]==0:
        From[2]=0
    To[1]=To[1]+IlePrzelać