#rut, d, m, f=2, s=0, res:entero
#dv :texto
f=2
s=0

#Escribir "ingrese su rut sin dv"
#Leer rut
rut=(int)(input("rut sin dv "))

#mientras
while rut>0:
  d=rut%10
  rut=rut//10

  m=d*f
  f=f+1
  if f>7:
    f=2
  s=s+m

s=s%11
res=11-s

if res>=0 and res<=9:
  dv=res
elif res==10:
  dv="k"
elif res==11:
  dv=0
else:
  dv="algo raro pasó"

print("Su dv es: ",dv)
