#ejemplo para crear y llenar arreglo de n elementos
n=(int)(input("Ingrese tamaño del cuestionario"))
arreglo=[]

#para i desde .. hasta ...
#para i=0 hasta i=n
for i in range(n):
  arreglo.append(i*2)
print(arreglo)

#ejemplo ingreso datos por teclado en un arreglo
rec=[]

#con una variable
a=input("dale datos a tu arreglo")
rec.append(a)

#directo desde teclado
rec.append(input("dale datos a tu arreglo "))

#directo desde teclado con ciclo
for i in range(5):
  rec.append(input("dale datos a tu arreglo "))

#ejemplo validador para número positivo
numpos=0
while numpos<1:
  numpos=(int)(input("Ingrese un positivo "))


#ejemplo validador para aceptaro solo a, b o c
res="d"
while res!="a" and res!="b" and res!="c":
  res=(input("Ingrese respuesta "))


#ejemplo crear arreglo y darle valor(es)
arreglo=[]
arreglo.append("a")
print(arreglo)


#ejemplos uso de elementos de un arreglo
sumatoria=arreglo[0]+arreglo[1]+arreglo[2]+arreglo[3]+arreglo[4]
print(sumatoria)

arreglo[0]==arreglo[4]

for i in range(5):
  print(arreglo[i])

#ejemplo arreglos de frutas
frutas=[]
frutas.append("manzana")
print(frutas)
frutas.append("pera")
frutas.append("piña")
frutas.append("Pera")
frutas.append("Piña")

frutas[1]==frutas[3]

#ejemplo arreglo con números
numeros=[]

numeros.append(1)

numeros.append(0)
numeros.append(4)
numeros.append(5)

numeros[0]+numeros[3]
