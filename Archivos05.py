#Que hace el siguiente código?

dd={"a":"@","e":"ê","i":"1","o":"ö","u":"û","E":"3","O":"0"}
stxt= "Ola tengo problemas de Escritura"
respuesta=""
for i in stxt:
  if i in dd:
    e=dd[i]
  else:
    e=i
  respuesta=respuesta+e
  
print(respuesta)

#Pasar proceso anterior a función

def modtex(stxt):
  dd={"a":"@","e":"ê","i":"1","o":"ö","u":"û","E":"3","O":"0"}
  respuesta=""
  for i in stxt:
    if i in dd:
      e=dd[i]
    else:
      e=i
    respuesta=respuesta+e
  return respuesta

stxt= "Ola tengo problemas de Escritura"

print(modtex(stxt))

#abrir archivo y revisar contenido
f=open("texto.txt","r")
texto=f.read()
f.close()
print(texto)

#uso función y reviso
texto=modtex(texto)
print(texto)

#guardo en archivo
f=open("texto.txt","w")
f.write(texto)
f.close()

#vuelvo a abri el archivo y revisar contenido
f=open("texto.txt","r")
texto=f.read()
print(texto)
