#ahorcado v1
from random import randint 

#diccionario como fuente de palabras
words={0:"hola",1:"mundo",2:"televisor"}

#numero al azar para buscar la palabra
pnumber=randint(0,len(words)-1)

#ciclo que crea un arreglo letra a letra con la palabra
word=[char.upper()  for char in words[pnumber]]

#arreglo que se motrará para jugar con guiones en vez de letras
showord=[" _ " for i in range(len(word))]

#arreglo que tendrá las letras usadas
used=[]

#contrador de vidas iniciales
lives=10

#variable booleana que controla en juego
jugando=True

#variable que permita restar vida cuando corresponda
puesta=0

#muestra inicio del juego
print(str(showord)+" vidas: "+str(lives))
  
#ciclo que controla todo el juego
while(jugando==True):
  #jugador ingresa letra, revisa que sea solo una letra y se asegura que sea mayuscula
  letter = '' 
  while ((len(letter)!=1) or (letter in used)):
    letter = (input("Ingrese letra  ")).upper()
  #print(letter) #revisa como queda la letra recibida
  
  #guarda letra como usada
  used.append(letter)
  #print(str(used))
  
  #ciclo para revisar letra en palabra
  for i in range(len(word)):
    if(word[i]==letter): #si la letra está en la palabra, la muestra en lugar de su guión
      showord[i]=" "+letter+" "
      puesta=puesta+1 #detecta si se puso la letra
    
  if(puesta==0): #decidir si resta vida, luego resetea
    lives=lives-1
  puesta=0

  print(str(showord)+" vidas: "+str(lives))
  
  if(lives==0):#cuando se acaban las vidas se detiene el juego
    jugando=False
    print("Perdiste")
  
  if ' _ ' not in showord: #si no quedan guiones en la palabra se declara ganador
    print("Ganaste")
    jugando=False
