#1
def do_it(q,p):
  if(p<= len(q)-1):
    return q[p]
  else:
    return "Fuera de Rango"
  
ad=[1,2,3,4,5]
ap=[0,1,6,3,7,4,5]

av=[do_it(ad,i) for i in ap]
print(av)

#2
def do_it(e):
  if ord(e) ==65:
    return chr(ord(e))
  else:
    return "@"
  
smsg="AMOR ES AMAR"
aLin=[do_it(c) for c in smsg]

print(aLin)

#3
def do_it(p,q):
  ns=0
  if len(p)==len(q):
    for i in range(len(p)):
      ns=ns+p[i]+q[i]
  return ns
dd={"@":[1,2,3],"$":[-1,-2,-3],"&":[4,5,6]}
av=[do_it(dd["@"],dd["$"]), do_it(dd["@"],dd["&"]), do_it(dd["$"],dd["&"])]
print(av)

#4
def do_it(p):
  aa=[0,0,0,0,0,0]
  nl=len(p)-1
  for i in range(nl+1):
    aa[nl-i]=p[i]
  return aa

ab=["A",2,"@",3,4,"#"]
print(ab)

#5
ad=[4,3,5,0,-1]
ai=[1,1,2,-1,1]
nc=0
lok=3>2

while nc<3 and lok:
  for i in range(5):
    ad[i]+=ai[i]
  nc+=1
  
print(ad)

#6
stxt="Hola Mundo"
ni=0
while ni<11:
  print(stxt[0:ni])
  ni+=1

#7
ad=[2,3,4]
ap=[2,0,1]

for i in range(1,4):
  for j in range(1,3):
    for k in ap:
      print(i,j,k,ad[k])

