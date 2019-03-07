#Práctica 5 - Ejercicio 11 - José Alberto Martín
#Exercici 11
#Escriu un programa per a jugar a endivinar un nombre (l'ordinador “pensa” el
#nombre i l'usuari l'ha d'endevinar). El programa comença demanant entre què
#nombres està el nombre a endevinar, s'”inventa” un nombre a l'atzar i després
#l'usuari va probant valors i el programa va decidint si són
#massa grans o pe.tits. Pista:
#import random
#import time
#random.seed(time.time())
#minim = int(raw_input("Vamor minim: "))
#maxim = int(raw_input("Vamor maxim: "))
#secret = random.randint(minim, maxim)
#Valor mínim: 0
#Valor màxim: 100
#A veure si endevines un nombre sencer entre 0 y 100.
#Escriu un nombre: 20
#Massa petit! Torna a probar: 30
#Massa gran! Torna a probar: 27
#Correcte! Ho has intentat 3 vegades.

import random
encontrado= False

minim=int(input("Valor mínimo: "))
maxim=int(input("Valor máximo: "))
secret=random.randint(minim,maxim)
intentos=0

print ("A ver si adivinas un número entero entre",minim,"y",maxim)

num=int(input("Escribe un número "))

while not encontrado:
    if num<secret:
        num=int(input("Demasiado pequeño, vuelve a intentarlo: "))
        intentos+=1
    elif num>secret:
        num=int(input("Demasiado grande, vuelve a intentarlo: "))
        intentos+=1
    else:
        if num==secret:
            encontrado= True

print ("¡Muy bien! El número secreto era", secret,"y lo has encontrado en", intentos,"intentos")
    
