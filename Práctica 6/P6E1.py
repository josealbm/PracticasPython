#Práctica 6 - Ejercicio 1 - José Alberto Martín Marí
#Escribe un programa que permita crear una lista de palabras.
#Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista.
#Por último, el programa tiene que escribir la lista.

lista=[]
palabras=int(input("Dime cuántas palabras va a tener tu lista "))

for i in range(palabras):
    palabra=input("Dime la palabra %d: "%(i+1))
    lista.append(palabra)

print ("La lista creada es: ", lista,)
