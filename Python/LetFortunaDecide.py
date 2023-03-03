import random
import os
import time
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
print('------------------------------')
print("Let Fortuna guide thy decision")
print('------------------------------')
time.sleep(1)
clearConsole()
Choices=[[0]]
print('------------------------------')
a=int(input(("How manny options do you have:")))
print('------------------------------')
time.sleep(1)
print("Enter them bellow")
time.sleep(0.1)
for integ in range(a):
    temp_mem=input("-")
    Choices.append(temp_mem)
print('------------------------------')
clearConsole()

print('------------------------------')
print("Letting the dice roll ...")
print('------------------------------')

def TrueRandome(HM):
    OneRandome=random.randint(1,100)
    RandomeNums=[]
    for ing in range(OneRandome):
        time.sleep(0.1)
        RandomeNums.append(random.randint(1, HM))
    while len(RandomeNums)>1:
        todel=random.randint(1,len(RandomeNums))
        del RandomeNums[(todel-1)]
    return(RandomeNums[0])

Choice=TrueRandome(a)

clearConsole()
print('------------------------------')
print('You should choose nr',Choice)
print('------------------------------')
time.sleep(0.1)
print('which was,','"',Choices[Choice],'"')
print('------------------------------')
b=input()