mat=[['A','C'],['D','C'],['A','A'],['D','A']]

mat=sorted(mat, key=lambda x:x[1])[::-1]
mat=sorted(mat,key=lambda x:x[0])

print(mat)