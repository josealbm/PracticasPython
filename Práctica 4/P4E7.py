#Práctica 4 Ejercicio 7 - José Alberto Martín
#Escriu un programa que demani l'alçada d'un triangle i ho dibuixi de la següent manera:
#Alçada del triangle: 4
#****
#***
#**
#*


alt=int(input("Escribe la altura de tu triángulo "))
asterisco="*"

for i in range(alt,0,-1):
    print (i*asterisco)
