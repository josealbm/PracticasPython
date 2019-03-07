#Práctica 6 - Ejercicio 9 - José Alberto Martín Marí
#Escribe un programa que permita crear una lista de 
#palabras y que, a continuación, cree una 
#segunda lista con las palabras de la primera, pero 
#sin palabras repetidas (el orden de las palabras 
#en la segunda lista no es importante). 

lista=[]
palabras=int(input("Dime cuántas palabras va a tener tu lista "))

for i in range(palabras):
    palabra=input("Dime la palabra %d: "%(i+1))
    lista.append(palabra)

print ("La lista creada es: ", lista)

lista2=lista[:]

for i in lista2:
    if lista2.count(i)>1:
        lista2.remove(i)
        
print ("La lista sin repeticiones es: ", lista2)

