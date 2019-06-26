#1 haga un script que guarde 10 veces "hola mundo" en salida.txt

f=open("salida.txt","w")
for i in range(10):
  f.write("Hola Mundo"+"\n")
f.close()


#2 para el arreglo aData haga un script que guarde en out.txt los valores de aData

aData=[1,2,3,"Estoy Frito",4]
f=open("out.txt","w")
for i in aData:
  f.write(str(i)+"\n")
f.close()


#3 extraiga usando readline() y split() la frase "no cacho nada" desde el archivo datos.txt

#constructor de datos.txt
datos="a,b,c,no cacho nada,1,2,3,@"
f=open("datos.txt","w")
f.write(datos+"\n")
f.close()

#solución ejercicio
f=open("datos.txt","r")
d=f.readline()[:-1].split(",")
print(d[3])


#4 usando readlines() y split() haga un script que entregue la suma de cada fila de info.txt

#constructor de info.txt
info="1,2,3,4,5\n3,4,5,6,7\n5,6,7,8,9\n"
f=open("info.txt","w")
f.write(info)
f.close()

#solución ejercicio
f=open("info.txt","r")
suma=[]
ns=0
aD=f.readlines()
for i in aD:
  t=i[:-1].split(",")
  for v in t:
    ns=ns+int(v)
  suma.append(ns)
  ns=0
  
print(suma)
