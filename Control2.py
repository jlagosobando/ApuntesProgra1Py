import math

#Ej1
aB=[1,2,3,-1,-2,-3]

ns=0
for e in aB:
    ns=ns+e
print("suma ej1 metodo1",ns)

ns=0
for i in range (len(aB)):
    ns=ns+aB[i]
print("suma ej1 metodo2",ns)


#Ej2
aP=[1,3,4,5,2,3,6,7]
aQ=[7,6,0,3,2,1,4,5]

print("Ej2 punto A\n")

ns=0
for i in range (len(aQ)):
    ns=ns+aP[aQ[i]]
print("suma ej2 puntoA metodo1",ns)

ns=0
for e in aQ:
    ns=ns+aP[e]
print("suma ej2 puntoA metodo2",ns)

print("\nEj2 punto B\n")

ns=0
for i in range (len(aQ)):
    ns=aP[i]*aQ[i]
    print("mult ej2 puntoB metodo1 pos",i,  ": ",ns)
print("\n")

for i in range (len(aP)):
    ns=aP[i]*aQ[i]
    print("mult ej2 puntoB metodo2 pos",i,  ": ",ns)
print("\n")


#Ej3
aRadios=[1,2,3,4,5]

for e in aRadios:
    p=2*math.pi*e
    print("perimetro ej3 metodo1 ele ",e," : ",p)
print("\n")

for i in range(len(aRadios)):
    p=2*math.pi*aRadios[i]
    print("perimetro ej3 metodo2 pos ",i," : ",p)
print("\n")


#Ej4
aI=[0,1,2,1,2,1,2,0]
aT=[[1,2,4],[3,2,4],[-7,-9,-9]]

print("punto a\n")

for i in aI:
    print(aT[i][:])
print("\n")

print("punto b\n")

for i in aI:
    print(aT[i][0:3])
print("\n")

print("punto c\n")

for i in aI:
    print(aT[i][0::2])
print("\n")


#Ej5
sTxt="Hola raton con cola"

print("punto a\n")
print(sTxt[0::3])
print("\n")

print("punto b\n")
print(sTxt[1::2])
print("\n")

print("punto c\n")
print(sTxt[0:4])
print("\n")

print("punto d\n")
print(sTxt[4::-1])
print("\n")


#Ej6
d={
'a': [1,2,3,4],
'b': [[1,2,3],[2,3,4],[5,6,7]],
'c': (1,2,-3,4),
'd': "Hola raton con cola"}

print("punto a\n")
for e in d['c']:
    print(e)
print("\n")

print("punto b\n")
for e in d['b'][0]:
    print(e)
print("\n")

print("punto c\n")
for e in d['b'][2]:
    print(e)
print("\n")


#Ej7

print("metodo1\n")
print(d['c'][1])

print("\n")

print("metodo2\n")
print(d['c'][2])
