v=[1,2,3,4,5,6,7,8,9]

def RowMov(R,N):    #ROW NUMBER
    L=R[:]
    for g in range(len(R)):
        L[g]=R[((g-N)%(len(R)))]
    return L

v=RowMov(v,len(v))
print(v)