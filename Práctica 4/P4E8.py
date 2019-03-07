#Práctica 4 Ejercicio 8 - José Alberto Martín
#Escriu un programa que demani l'amplada d'un triangle i ho dibuixi de la següent manera:
#Alçada del triangle: 4
#*
#**
#***
#****
#***
#**
#*

amp=int(input("Escribe la amplitud de tu triángulo "))


for i in range(amp):
    ancho=i*"*"
    print (ancho)

for j in range (amp, 0, -1):
    alto=j*"*"
    print (alto)
