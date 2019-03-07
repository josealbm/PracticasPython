#Práctica 4 Ejercicio 5 - José Alberto Martín
#Escriu un programa que demani l'amplada i alçada d'un rectangle i ho dibuixi de la següent
#manera:
#Amplada del rectangle: 5
#Alçada del rectangle: 3
#*****
#*****
#*****


alt=int(input("Escribe la altura de tu rectángulo "))
base=int(input("Escribe la base de tu rectángulo "))
ast="*"


for i in range(alt):
    res=alt*"*"
    print (res)

    for j in range(base):
        print (j*res)
