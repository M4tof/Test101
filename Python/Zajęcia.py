#Stats ={"name":"","cpu":0,"gpu":0,"disc":0,"ram":0,"price":0}

Komputery=[]
for ind in range(int(input())):
    Dane=input().split()
    temp={"name":str(Dane[0]),"cpu":int(Dane[1]),"gpu":int(Dane[2]),"disc":int(Dane[3]),"ram":int(Dane[4]),"price":int(Dane[5])}
    Komputery.append(temp)
    temp={}         #Komputery lista zlozona z Dictow


for ind2 in range(int(input())):
    Brane=Komputery[:]    
    Wymagania=input().split()   #np: gpu:10 cpu:150
    for i in range(len(Wymagania)): 
        Test=(Wymagania[i]).split(':') #np gpu:10
        Nazw=Test[0]
        Wartosc=int(Test[1])
        Temp=[]
        for j in range(len(Brane)):
            if Brane[j][Nazw] >= Wartosc:
                Temp.append(Brane[j])
        Brane=Temp
        print(Brane)