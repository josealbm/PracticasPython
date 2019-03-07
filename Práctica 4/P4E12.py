#Práctica 4 Ejercicio 12 - José Alberto Martín
#Escriu un programa que demani un nombre i escrigui si és primer o no.
#Dona'm un nombre:
#123
#El nombre 123 no és primer
#Dona'm un nombre:
#127
#El nombre 127 és primer

n=int(input("Dame un número "))
divisores=0

for i in range(1, n+1):
    if n%i==0:
        divisores+=1
if divisores<=2:
        print ("El número",n,"es primo")
else:
        print ("El número",n,"no es primo")

