#distintas formas de crear arreglos
a=[]
b=[1,2,3,4,5,6]
c=[["a","b","c"],["d","e","f"]]

print(a)
print(b)
print(c)

#agregar elementos a un arreglo con append
a.append(1)
a.append(2)
print(a)

#agregar elementos a un arreglo con extend
a.extend(b)
print(a)

#agregar elementos a un arreglo con insert y modificar celda
a[0]=7
a.insert(1,"X")
print(a)

#eliminar elementos de un arreglo remove
a.remove("X")
print(a)

#eliminar elementos de un arreglo del
del a[0]
print(a)

