N=input().split()
H=int(N[1])
N=int(N[0])

Trees=[]
for ind in range(N):
    Trees.append(list(map(int,input().split())))

Trees=sorted(Trees,key=lambda x:x[0])
print(Trees)