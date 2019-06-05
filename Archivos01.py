#abrir archivo para para escritura, si archivo no existe se crea
f=open("archivo.txt","w")
f.write("test")
f.close()

#abrir archivo para escritura,  guarda enteros
f=open("archivo.txt","w")
for i in range(21):
    f.write(str(i))
f.close()

#abrir archivo para escritura,  guarda enteros con salto de linea
f=open("archivo.txt","w")
for i in range(21):
    f.write(str(i)+"\n")
f.close()

#abrir archivo para escritura,  guarda textos con salto de linea
f=open("archivo.txt","w")
for i in range(60, 94):
    f.write("ascii "+str(i)+" "+chr(i)+"\n")
f.close()

#abrir archivo para lectura, lee todo de una vez
f=open("archivo.txt","r")
text=f.read()
print(text)

#abrir archivo para lectura, lee solo una linea
f=open("archivo.txt","r")
texto=f.readline()
print(texto)

#abrir archivo para lectura, lee linea a linea e imprime mietras no se llegue al final del archivo
f=open("archivo.txt","r")
while True:
    texto=f.readline()
    if texto=="":
        break
    print(texto)

#abrir archivo para lectura, lee linea a linea e imprime
f=open("archivo.txt","r")
for line in f:
    print(line)
    
#abrir archivo para lectura, lee linea a linea e imprime con frase
i=1
f=open("archivo.txt","r")
for line in f:
    print("linea "+str(i)+" "+line)
    i=i+1

#abrir archivo para lectura, lo recorre linea a linea, aplica strip, transforma a entero e imprime
f=open("archivo.txt","r")
for line in f:
    line=line.strip()
    number=int(line)
    print (number)
    
