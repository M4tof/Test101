import random

a='0'


for i in range(4999):
    a+=' '+str(random.randint(-1000,1000))

print(a)