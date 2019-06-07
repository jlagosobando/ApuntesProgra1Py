aB=[[1,0,3],[6,4,5]]

filas=len(aB)
colum=len(aB[0])

f=open("archivo.txt","w")

for e in range(len(aB)):
    for i in range(len(aB[e])):
        f.write(str(aB[e][i])+"\n")
f.close()
print(aB)


f=open("archivo.txt","r")

aC=[[None,None,None],[None,None,None]]

for e in range(len(aC)):
    for i in range(len(aC[e])):
        aC[e][i]=int(f.readline().strip())
print(aC)
f.close()
