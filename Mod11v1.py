#pedir rut
ruto=input("rut sin dv ")
largo=len(ruto)
rut=int(ruto)

#core
f=2
suma=0

for i in range(largo): #while rut>0:
  d=rut%10
  m=d*f
  rut=rut//10
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
  print("algo raro pasó")

print(dv)

#abrir archivo para escritura,  guarda rut
f=open("archivo.txt","w")
f.write(str(ruto)+"-"+str(dv))
f.close()
