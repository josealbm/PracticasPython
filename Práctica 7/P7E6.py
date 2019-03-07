#Práctica 7 - Ej 6 - José Alberto Martín
#Escribe un programa que lea el nombre de una persona y
#un carácter, le pase estos datos a una función  que
#comprobará    si  dicho  carácter  está  en  su  nombre.
#El  resultado  de  dicha  función  lo imprimirá el programa
#principal por pantalla

def caracteres(nom,letra):
    contador=0
    for i in nom:
        if i==letra:
            contador+=1
    return print ("En el nombre", nombre,"el carácter", letra,"aparece", contador,"veces")

nombre=input("Escríbeme un nombre: ")
letra=input("¿Qué caracter quieres comprobar si aparece? ")

caracteres(nombre,letra)
