#Práctica 4 Ejercicio 2 - José Alberto Martín Marí
#Escriu un programa que demani dos nombres i escrigui quins nombres son parells i quins són
#senars (=”impares”) des del primer fins al segon.

a=int(input("Escribe el primer número "))
b=int(input("Escribe un número mayor que el primero "))

for i in range(a, b+1):
    if (i%2==0):
        print ("Tu número", i,"es par")
    else:
        print ("Tu número", i,"es impar")
            
