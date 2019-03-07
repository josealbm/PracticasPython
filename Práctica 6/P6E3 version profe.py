#Práctica 6 - Ejercicio 3 - José Alberto Martín Marí
#Escribe un programa que permita crear una lista de palabras y que,
#a continuación, pida dos palabras y sustituya la primera por la
#segunda en la lista. 

lista=[]
palabras=int(input("Dime cuántas palabras va a tener tu lista "))

for i in range(palabras):
    palabra=input("Dime la palabra %d: "%(i+1))
    lista.append(palabra)

print ("La lista creada es: ", lista,)
nom=input("Ahora dime la palabra que quieras substituir: ")
nom2=input("Escribe la que quieres introducir: ")
while nom in lista:
    lista[lista.index(nom)]=nom2


print ("La lista es ahora:",lista,)

