Butelki=[]

for ind in range(int(input())):
  A=input().split()
  A[1]=int(A[1])
  A[2]=int(A[2])
  A[3]=int(A[3])
  Butelki.append(A)

Butelki=sorted(Butelki)

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

for jnd in range(int(input())):
  F=input().split()
  From=F[0]
  To=F[1]
  for j in range(len(Butelki)):
    if Butelki[j][0]==From:
      From=Butelki[j]
    if Butelki[j][0]==To:
      To=Butelki[j]
  From,To=przelej(From,To)    
  
for g in range(len(Butelki)):
  print(Butelki[g][1])