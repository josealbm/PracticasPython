#Pràctica 4 exercici 9 - José Alberto Martín Marí
#Escriu un programa que demani l'amplada i l'alçada d'un rectangle i ho dibuixi de la següent
#manera:
#Amplada del rectangle: 5
#Alçada del rectangle: 4
#*****
#* *
#* *
#*****


base=int(input("Dime la base de tu rectángulo "))
altura=int(input("Dime la altura de tu rectángulo "))


for i in range(altura):
        if i == 0 or i == altura-1:
            print(base*'*')
        else: 
            print("*"+" "*(base-2)+"*")   
