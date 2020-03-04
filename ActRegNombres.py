#1 para el siguiente arreglo
Est=["Juan","Diego","Alicia","Gloria"]

#2 guarde en un archivo el contenido del arreglo, un nombre por linea
file=open("est.txt","w")

for e in Est:
  file.write(e+"\n")

file.close()

#3 pida al usuario los apellidos para cada estudiante por teclado
#modifique al arreglo agregando esta info, sin aumentar dimensionalidad ni número de casillas

for i in range(len(Est)):
  apellido=input("Escriba apellido "+str(i)+": ")
  Est[i]=Est[i]+" "+apellido

print(Est)


#cree un nuevo arreglo, agregando una nueva dimensión
#para cada estudiante en Est, deberá asociar un registro academico ingresado por teclado

Registro=[]

for e in Est:
  reg=input("ingrese n° de registro de "+str(e)+" ")
  temp=[e,reg]
  Registro.append(temp)

print(Registro)

#guarde en un archivo reg.txt el resultado de su arreglo, un estudiante por linea
#separando nombre y registro por un espacio

file=open("reg.txt","w")

for e in Registro:
  file.write(e[0]+" "+str(e[1])+"\n")

file.close()
