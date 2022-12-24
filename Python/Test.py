v1=['A',3,1,5]
v2=['B',0,2,4]      #Nazwa , sok,woda,pojemnosc
v3=['C',2,0,4]

def przelej(x,y): #from to
    Can_Take=y[3]-y[1]-y[2]
    Can_Provide = x[1]+x[2]
    if Can_Take >= Can_Provide:
        Will_do=Can_Provide
    else:
        Will_do=Can_Take
    Stosunek=0
    try:
        Stosunek=x[1]/(x[2]+x[1])
    except:
        pass

    y[1]=y[1]+ ( Will_do*Stosunek)
    y[2]=y[2] +(Will_do*(1-Stosunek))

    x[1]=x[1]-(Will_do*Stosunek)
    x[2]=x[2]-(Will_do*(1-Stosunek))
    return [x,y]


v2,v3=przelej(v2,v3)
v3,v1=przelej(v3,v1)

print(v1)
print(v2)
print(v3)