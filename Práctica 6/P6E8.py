#Práctica 6 - Ejercicio 8 - José Alberto Martín Marí
#Escribe un programa que permita crear una lista de 
#palabras y que, a continuación, ordene la lista 
#por orden alfabético. 

lista=[]
palabras=int(input("Dime cuántas palabras va a tener tu lista "))

for i in range(palabras):
    palabra=input("Dime la palabra %d: "%(i+1))
    lista.append(palabra)

print ("La lista creada es: ", lista)

for i in range(4):
    for j in range(4-i):
        if lista[j]>lista[j+1]:
            aux=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=aux

print ("La lista ordenada es: ", lista)
