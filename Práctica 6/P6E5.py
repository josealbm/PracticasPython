#Práctica 6 - Ejercicio 5 - José Alberto Martín Marí
#Escribe un programa que permita crear dos listas de palabras
#y que, a continuación, elimine de la primera lista los nombres
#de la segunda lista.


lista=[]
palabras=int(input("Dime cuántas palabras va a tener tu lista "))

for i in range(palabras):
    palabra=input("Dime la palabra %d: "%(i+1))
    lista.append(palabra)

print ("La lista creada es: ", lista,)

lista2=[]
palabras2=int(input("Dime cuántas palabras tiene la lista de palabras\
a eliminar: "))

for i in range(palabras2):
    palabra2=input("Dime la palabra %d: "%(i+1))
    lista2.append(palabra2)

print ("La lista de palabras a eliminar es: ",lista2,)

for i in lista2:
    lista.remove(i)

print ("La lista resultante es: ",lista,)
