#Ejercicios con arreglos

#sumar elementos de arreglo bidimensional
def sumarreglos2(arreglo):
    ns=0
    for i in range(len(arreglo)):
        for j in range(len(arreglo[i])):
            ns=ns+arreglo[i][j]
    return ns
    
aB=[[1,2,3],[4,5,6]] #suma 21
aC=[[1,2,3],[4,5,6],[7,8,9]] #suma 45

print(sumarreglos2(aB))
print(sumarreglos2(aC))

#para los arreglos dados:
aU=[1,2,3,4,5,6]
aT=[3,4,5,6]

#suma 2 arreglos unidimensionales (limitado por el más corto)
#1+3,2+4,3+5,4+6

def suma2arreglos(arreglo1,arreglo2):
    if(len(arreglo1)>len(arreglo2)):
        largo=len(arreglo2)
    else:
        largo=len(arreglo1)
    resultado=[arreglo1[i]+arreglo2[i] for i in range(largo)]
    return resultado
#uso    
print(suma2arreglos(aU,aT))

#suma 2 arreglos unidimensionales sin importar largo de estos
#para los mismo arreglos anteriores 1+3,2+4,3+5,4+6,5+0,6+0

def suma2arreglos2(arreglo1,arreglo2):
    if(len(arreglo1)<len(arreglo2)):
        largo=len(arreglo2)
    else:
        largo=len(arreglo1)

    resultado=[0]*largo

    for i in range(largo):
        try:
            elemento1=arreglo1[i]
        except:
            elemento1=0
        try:
            elemento2=arreglo2[i]
        except:
            elemento2=0
        resultado[i]=elemento1+elemento2
    return resultado

#uso
print(suma2arreglos2(aU,aT))
