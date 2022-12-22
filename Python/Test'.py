from functools import cache
import time
Licz=list(map(int,input().split()))

@cache
def Summ():
    return sum(Licz[N[0]:N[1]+1])


for i in range(int(input())):
    N=list(map(int,input().split()))
    start_time = time.time()
    print(Summ())
    print(time.time() - start_time)