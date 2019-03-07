#Pràctica 4 exercici 10 - José Alberto Martín Marí
#Exercici 10 (opcional)
#Escriu un programa que demani l'alçada d'un triangle i ho dibuixi de la següent manera:
#Alçada del triangle:
# 5
#    *
#   ***
#  *****
# *******
#*********

alt=int(input("Dime la altura del triángulo que quieres hacer "))

for i in range(alt+1):
    print ((" "*(alt-i))+((i)*"*")+((i-1)*"*"))
