#Práctica 6 - Ejercicio 7 - José Alberto Martín Marí
#Escribe un programa que permita crear dos listas de palabras y que,
#a continuación, escriba las
#siguientes listas (en las que no debe haber repeticiones):
#• Lista de palabras que aparecen en las dos listas
#• Lista de palabras que aparecen en la primera lista, pero no en la segunda
#• Lista de palabras que aparecen en la segunda lista, pero no en la primera
#• Lista de palabras que aparecen en ambas listas

lista=[]
palabras=int(input("Dime cuántas palabras va a tener tu lista: "))

for i in range(palabras):
    palabra=input("Dime la palabra %d: "%(i+1))
    lista.append(palabra)

print ("La lista creada es: ", lista,)

lista2=[]
palabras2=int(input("Dime cuántas palabras va a tener la segunda lista: "))

for i in range(palabras2):
    palabra2=input("Dime la palabra %d: "%(i+1))
    lista2.append(palabra2)

print ("La segunda lista es: ", lista2,)
repe=[]
sololista=lista[:]
sololista2=lista2[:]
listacompleta=[]

for i in lista:
    for j in lista2:
        if i==j:
            repe.append(i)

for i in lista:
    for j in lista2:
        if i==j:
            sololista2.remove(i)
    
for i in lista2:
    for j in lista:
        if i==j:
            sololista.remove(i)
            
print ("Las palabras que aparecen en las dos listas son", repe,)
    
print ("Las palabras que aparecen sólo en la primera lista son: ", sololista,)
        
print ("Las palabras que sólo aparecen en la segunda lista son: ", sololista2,)

for i in sololista:
    listacompleta.append(i)
for i in sololista2:
    listacompleta.append(i)
for i in repe:
    listacompleta.append(i)

print ("Todas las palabras son: ", listacompleta,)
                   
        
            
