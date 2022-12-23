s = input()
#print(sum(s.count(x)%2 for x in set(s)) < 2)
print(sum( s.count( int(s) )%x for x in range( 2,int(s) ) ) ==0)


#for i in range(2,int(s)):
    #if int(s)%i==0:
        #print(False)
        