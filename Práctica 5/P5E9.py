#Práctica 5 - Ejercicio 9 - José Alberto Martín Marí
#Escriu un programa que et demani noms de persones i els seus números de telèfon. Per a
#terminar de escriure nombres i numeros s'ha de pulsar Intro quan et demani el nom. El programa
#termina escribint noms i números de telèfon. Nota: La llista en la que es guarden els noms i
#números de telèfon és [ [nom1, telef1], [nom2, telef2], [nom3, telef3], etc]
#Dona'm un nom: Sergi González
#Dona'm el telèfon: 971971971
#Dona'm un nom: Macarena Gómez
#Dona'm el telèfon: 971999999
#Dona'm un nom: Pasqual Ribot
#Dona'm el telèfon: 666555444
#Dona'm un nom:
#Els noms i telèfons són:
#Sergi González: 971971971
#Macarena Gómez: 971999999
#Pasqual Ribot: 666555444
nombres=[]
telf=[]
lista=[nombres, telf]
nom=input("Dime un nombre ")

while nom!="":
    nombres.append(nom)
    num=input("Dime un teléfono ")
    telf.append(num)
    nom=input("Dime un nombre ")

print ("Los nombres y teléfonos son: ")
for i in range(len(lista)+1):
       print (nombres[i]+": " + telf[i])
