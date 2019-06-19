#1

def Get_Data(aData):
 sL = ''
 for e in aData:
  sL += str(e) + ','
  
 sL = sL[:-1] + '\n'
 return sL

aData = [1,2,3,4,5,6,7,9,0x0A]
 
f = open('datos.txt','w') # Abrimos Modo Escritura (w)
f.write(Get_Data(aData))
f.close()

#2

def Get_Data(aData):
 sL = ''
 for a in aData:
  for b in a:
    sL += str(b) + ','
  sL = sL[:-1] +"\n"
  
 return sL

aD = [ [1,2,3,4,5],[4,6,3,1,0],[2,5,8,4,9],[4,4,4,3,2] ]

fh = open('lineas.txt','w')
fh.write(Get_Data(aD))
fh.close()

#3

def Get_MSG(nV):
 return 'El valor es: ' + str(nV) + '\n'

aD = [1,2,3,4,5,6,7,9,0x0A]

fh = open('msg.txt','w')
fh.write(Get_MSG(aD))
fh.close()

#4

t1 = t2 = [] 
Suma = 0

fh = open('valores.csv.txt')
aD = fh.readlines()
fh.close()

for e in aD:
 t1 = e[:-1].split(',')
 for v in t1:
   Suma += int(v)
 t2.append(Suma)
 Suma = 0
t2
