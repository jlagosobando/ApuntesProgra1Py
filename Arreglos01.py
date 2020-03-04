Frutas=["Manzana","Pina","Uva"]
for elemento in Frutas:
  print(elemento)


Curso=["Estrella", "b", "..."]
print(Curso[0])

for alumno in Curso:
  print(elemento)
  
  
Persona=["Juan","02/08/1990","Ing."]
Persona2=["Diego","23/11/1999","ICI"]
print("Mi nombre es "+Persona[0]+" naci el "+Persona[1]+" y soy "+Persona[2])
print("Mi nombre es "+Persona2[0]+" naci el "+Persona2[1]+" y soy "+Persona2[2])

Personas=[["Juan","02/08/1990","Ing."],
          ["Diego","23/11/1999","ICI"],
          ["Juan","02/08/1990","Ing."],
          ["Diego","23/11/1999","ICI"],
          ["Juan","02/08/1990","Ing."],
          ["Diego","23/11/1999","ICI"]]

for humanoide in Personas:
  print("Me llamo "+humanoide[0]+" naci el "+humanoide[1]+" y soy "+humanoide[2])
  
Colores=[["azul","rojo","amarillo"],["verde","naranjo"]]

for cat in Colores:
  print("____")
  for color in cat:
    print(color)
