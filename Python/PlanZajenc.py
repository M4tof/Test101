N=input().split()
M=int(N[1])
N=int(N[0])

def RowMov(R,N):    #ROW NUMBER
    L=R[:]
    for g in range(len(R)):
        L[g]=R[((g-N)%(len(R)))]
    return L

def obrot(a): 
    mat2=[]
    for n in range(len(a[0])):
        temptab=[]
        for n2 in range(len(a)):
            temptab.append(a[n2][n])
        mat2.append(temptab)
    return mat2

mat1=[]
matf=[]
for i in range(N):
    mat1.append(list(map(int,input().split())))
for j in range(N):
    matf.append(list(map(int,input().split())))

if mat1==matf:
    print("TAK")
    quit()


mat3=mat1[:]
for y in range(N):
    for z in range(1,N-1):
        mat4=mat3[:]
        mat4[y]=RowMov(mat3[y],z)
        if mat4==matf:
            print("TAK")
            quit()

mat5=obrot(matf)
mat3=obrot(mat1[:])

for y in range(M):
    for z in range(1,M-1):
        mat4=mat3[:]
        mat4[y]=RowMov(mat3[y],z)
        print(mat4)
        if mat4==mat5:
            print("TAK")
            quit()

print("NIE")