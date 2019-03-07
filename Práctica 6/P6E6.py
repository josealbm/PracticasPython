#Práctica 6 - Ejercicio 6 - José Alberto Martín Marí
#Escribe un programa que permita crear una lista de palabras y que,
#a continuación, cree una segunda lista igual a la primera, pero al revés
#(no se trata de escribir la lista al revés, sino de crear una lista distinta). 

lista=[]
palabras=int(input("Dime cuántas palabras va a tener tu lista "))

for i in range(palabras):
    palabra=input("Dime la palabra %d: "%(i+1))
    lista.append(palabra)

print ("La lista creada es: ", lista,)
lista2=[]
for i in range(len(lista)-1, -1, -1):
    lista2.append(lista[i])
print ("La lista inversa es: ", lista2,)
