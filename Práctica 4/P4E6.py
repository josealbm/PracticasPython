#Práctica 4 Ejercicio 6 - José Alberto Martín
#Escriu un programa que demani l'alçada d'un triangle i ho dibuixi de la següent manera:
#Alçada del triangle: 4
#*
#**
#***
#****


alt=int(input("Escribe la altura de tu triángulo "))

for i in range(alt+1):
    print (i*"*")
