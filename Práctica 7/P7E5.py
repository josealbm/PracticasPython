#Práctica 7 - Ej 5 - José Alberto Martín
#Escribe un programa que te pida una frase y una vocal,
#y pase estos datos como parámetro a una 
#función  que  se  encargará  de  cambiar  todas  las  vocal
#es  de  la  frase  por  la  vocal  seleccionada. 
#Devolverá la función la frase modificada, y el programa principal
#la imprimirá:

def cambio(a,b):
    vocales=["a","e","i","o","u"]
    for i in vocales:
        if i in a:
            a=a.replace(i,b)
    print (a)

frase=input("Escribe una frase: ")
vocal=input("Dime qué vocal seleccionas: ")

cambio(frase,vocal)
