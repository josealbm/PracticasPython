#Práctica 5 - Ejercicio 10 - José Alberto Martín
#Escriu un programa que et demani els noms i notes d'alumnes. Si escrius una nota fora de
#l'interval de 0 a 10, el programa entendrà que no vols introduir més notes d'aquest alumne. Si no
#escrius el nom, el programa entendrà que no vols introduir més alumnes. Nota: La llista en la que
#es guarden els noms i notes és [ [nom1, nota1, nota2, etc], [nom2, nota1, nota2, etc], [nom3,
#nota1, nota2, etc], etc]
#Dona'm un nom: Héctor Quiroga
#Escriu una nota: 4
#Escriu una altra nota: 8.5
#Escriu una altra nota: 12
#Dona'm un altre nom: Inés Valls
#Escriu una nota: 7.5
#Escriu una altra nota: 1
#Escriu una altra nota: 2
#Escriu una altra nota: -5
#Dona'm un altre nom:
#Les notes dels alumnes són:
#Héctor Quiroga: 4.0 - 8.5


lista=[]
nom=input("Dime un nombre ")

while nom!="":
    alumno=[]
    alumno.append(nom)
    num=float(input("Escribe una nota "))
    while num>=0 and num<=10:
        alumno.append(num)
        num=float(input("Escribe otra nota "))
    lista.append(alumno)
    nom=input("Dime un nombre ")

print ("Las notas de los alumnos son: \n")
for i in range(len(lista)):
    for j in range(len(lista[i])):
        if j==0:
            print(lista[i][j]+": ")
        elif j==(len(lista[i])-1):
            print(lista[i][j])
        else:
            print(lista[i][j], end=" - ")
