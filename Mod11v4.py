def CalculaDV(x):
    x=str(x)
    x=int(x.replace(".",""))
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
     
print(CalculaDV("17.366.752"))

def VerificaRut(rut):
  rut=rut.split("-")
  cadena=rut[0]
  dv=rut[1]
  if(dv=="k" or dv=="K"):
    dv="K"
  else:
    dv=int(dv)

  if(CalculaDV(cadena)==dv):
    return True
  else:
    return False

print(VerificaRut("17.366.752-3"))
