#declaración variables iniciales
cadena=-1
f=2
suma=0

#ingreso de datos
while cadena<1:
  ruto=input("rut sin dv ")
  cadena=int(ruto)

#core
while cadena>0:
  dig=cadena%10
  cadena=cadena//10

  m=dig*f
  suma=suma+m
  
  f=f+1
  if f>7:
    f=2

suma=suma%11
suma=11-suma

if suma<10:
  dv=suma
elif suma==10:
  dv="k"
elif suma==11:
  dv=0
else:
  dv="algo raro pasó"

#abrir archivo para escritura,  guarda rut
f=open("archivo.txt","w")
f.write(str(ruto)+"-"+str(dv))
f.close()
