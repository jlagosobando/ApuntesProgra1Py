aB=[[1,0,3],[6,4,5]]

filas=len(aB)
colum=len(aB[0])

f=open("archivo.txt","w")
f.write(str(filas)+"\n")
f.write(str(colum)+"\n")

for e in range(len(aB)):
    for i in range(len(aB[e])):
        f.write(str(aB[e][i])+"\n")
f.close()
print(aB)

f=open("archivo.txt","r")
fil=int(f.readline().strip())
col=int(f.readline().strip())
aC=[[None,None,None],[None,None,None]]

for e in range(len(aC)):
    for i in range(len(aC[e])):
        aC[e][i]=int(f.readline().strip())
print(aC)
f.close()

f=open("archivo.txt","r")
fil=int(f.readline().strip())
col=int(f.readline().strip())
aD=[ [ int(f.readline().strip()) for y in range(col) ] for x in range(fil) ]
print(aD)
f.close()
