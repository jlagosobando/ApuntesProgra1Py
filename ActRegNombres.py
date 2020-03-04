#1 para el siguiente arreglo
Est=["Juan","Diego","Alicia","Gloria"]

#2 guarde en un archivo el contenido del arreglo, un nombre por linea
file=open("est.txt","w")

for e in Est:
  file.write(e+"\n")

file.close()

#3 pida al usuario los apellidos para cada estudiante por teclado
#modifique al arreglo agregando esta info, sin aumentar dimensionalidad ni número de casillas


#cree un nuevo arreglo, agregando una nueva dimensión
#para cada estudiante en Est, deberá asociar un registro academico ingresado por teclado


#guarde en un archivo reg.txt el resultado de su arreglo, un estudiante por linea
#separando nombre y registro por un espacio
