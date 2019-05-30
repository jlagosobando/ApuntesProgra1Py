#Ejercicios de funciones "más complejas"

#Codificar (y decodificar) un texto manipulando el valor ASCII de los caracteres sumándole 1.

#codificar
def codificar(textoStr):
    texto=""
    for i in range(len(textoStr)):
        b=(ord(textoStr[i]))
        b=b+1
        texto=texto+(chr(b))
    return texto

#decodificar
def decodificar(textoCod):
    texto=""
    for i in range(len(textoCod)):
        b=(ord(textoCod[i]))
        b=b-1
        texto=texto+(chr(b))
    return texto
    
#uso
sTxt="Hola raton con cola"

cod=codificar(sTxt)
print(cod)

decod=decodificar(cod)
print(decod)

#calcular el dv de un rut chileno

def CalculaDV(x):
    f=2
    s=0
    for i in range(len(str(x))):
        d=x%10
        x=x//10
        m=d*f
        f=f+1
        if(f>7):
            f=2
        s=s+m
    dv=s%11
    dv=11-dv
    if(dv<10):
        return dv
    if(dv==10):
        return "K"
    if(dv==11):
        return 0

#verificar si un rut es real
def VerificaRut(rut,dv):
    if(dv=="k"):
        dv="K"
    if(CalculaDV(rut)==dv):
        return True
    else:
        return False

#uso
print(CalculaDV(19199552))
print(VerificaRut(19199552,"K"))
