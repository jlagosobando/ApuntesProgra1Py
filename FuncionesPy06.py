#Ejercicios Guia "Simpáticos"
#1 periodista, ironman, batman

aDATA=[0x41,0x56,0x27,0x75,0x22,0x33,0x44]
aADD1=[6,3,5,1,4,2,0]
aADD2=[1,0,6,4,3,5,2]

def Get_1(n):
    return aADD1[n]

def Get_2(n):
    return aADD2[Get_1(n)]

def Get_Mem(n):
    return aDATA[Get_2(n)]

aBatman_=[4,3,2,1,0,5,6]
aIronMan=[Get_Mem(i) for i in aBatman_]

#IronMan estára conformado por:
#Get_Mem aplicado a los valores de aBatman_, es decir  4,3,2,1,0,5,6
#Si se rastrea el uso de funciones dentro de funciones dará que:
#Get_Mem llama a Get_2, Get_2 llama a Get_1 , y esta su vez va a sacar datos de aDD1
#para el primer valor de aBatman_ (4), se termina llamando a aDD1[4), 4
#luego vamos a buscar aADD2 [4] (el 4 del resultado anterior, no del primer elemento de aBatman_)
#con esto rescatamos el valor 3 desde aDD2
#llamamos finalmente al indice 3 de aDATA, 0x75 que en decimal es 117
#con esto se puede generalizar que el resultado obtenido viene de:
# aDATA[ aADD2[ aADD1[n] ] ]   con n siendo cada elemento de aBatman_

print(aIronMan)

#2 nave, uMenor, llave19

global nKEY
nKey=19

def Get_Secret(sMsg):
    sTxt=""
    for e in sMsg:
        nChar=ord(e)^nKey
        sTxt+=chr(nChar)
    return sTxt

def Put_Secret(sMsg):
    sTxt=""
    for e in sMsg:
        nChar=ord(e)^nKey
        sTxt+=chr(nChar)
    return sTxt

sM="Gv}t|3prar3wv3~|}|"

cod=Get_Secret(sM)
print(cod)

decod=Put_Secret(cod)
print(decod)

#3 barney, mensaje, completar

aMSG=[112,32,97,111,109,114,32,97,111,114,101,110,97,101,110,66,32,115,97,114,103,114,33,98,121]
aIND=["15","2","9","14","10","24","1","11","3","6","17","12","23","13","16","0","5","8","20","19","7","4","18","21","22"]

def Get_MSG(aPos):
    sMsg=""
    for e in aPos:
        sMsg+=chr(aMSG[int(e)])
    return sMsg

print(Get_MSG(aIND))

#4 nave, uct, bomba

def Get_XOR(a,b):
    return a^b

def Get_AND(a,b):
    return a&b

def Explota(aF):
    XOR_1=Get_XOR(int(aF[0]),int(aF[1]))
    XOR_2=Get_XOR(int(aF[2]),int(aF[3]))
    Explo=Get_AND(XOR_1,XOR_2)
    return Explo

aBits=[
["1","1","0","0"],
["1","0","1","1"],
["1","1","0","1"],
["1","0","0","1"]]

for e in aBits:
    if Explota(e):
        print("Si Explota")
        print(e)
    else:
        print("No Explota")
        print(e)

#5 Donald,Heavy,aOut

aBytes=[">ab>211","?*{#157","^!+&90","%$+>55"]

def Get_Data(sDato):
    nVal=int(sDato[4:])
    nMSB=nVal>>4
    nLSB=nVal&0xf
    nSWP=nLSB|nMSB
    return nSWP

aOut=[Get_Data(e) for e in aBytes]
print(aOut)
