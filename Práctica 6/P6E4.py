#Práctica 6 - Ejercicio 4 - José Alberto Martín Marí
#Escribe un programa que permita crear una lista de palabras y que,
#a continuación, pida una palabra y elimine esa palabra de la lista.

lista=[]
palabras=int(input("Dime cuántas palabras va a tener tu lista "))

for i in range(palabras):
    palabra=input("Dime la palabra %d: "%(i+1))
    lista.append(palabra)

print ("La lista creada es: ", lista,)
nom=input("Dime la palabra que quieres eliminar: ")
while nom in lista:
    lista.remove(nom)
print ("La lista es ahora:", lista,)
