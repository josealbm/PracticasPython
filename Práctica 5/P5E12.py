#Práctica 5 - Ejercicio 12 - José Alberto Martín Marí
#Escriu un programa per a jugar a endevinar un nombre (l'usuari pensa un nombre i el programa
#l'ha d'endevinar). El programa comença demanant entre què nombres està el nombre
#a endevinar i després intenta endevinar de què nombre es tracta. L'usuari va
#dient si el nombre que ha dit el programa és menor, major o igual al que s'ha cercat.
#Valor mínim: 0
#Valor màxim: 100
#Pensa un nombre entre 0 i 100 a ver si ho puc endevinar.
#És 50?: major
#És 75?: menor
#És 62?: menor
#És 56?: major
#És 59?: igual
#Gràcies per jugar amb jo
#Pots perfeccionar el programa fent (ampliació per a qui vagi molt sobrat):
#• que al principi el programa s'asseguri de què el valor màxim és superior al valor mínim.
#• Que el programa detecti “trampes”, per exemple, si quan dius “25” li deim”major” i al dir “26”
#li deim “menor”, el programa ha de dir que estam fent trampes i ha de deixar de jugar amb
#nosaltres.

encontrado= False

minim=int(input("Dime un valor mínimo "))
maxim=int(input("Dime un valor máximo "))

print ("Piensa un número entre", minim,"y", maxim,"e intentaré adivinarlo \n \
Tienes que contestarme si es mayor, menor o igual que el que piensas")

if maxim<=minim:
    maxim=int(input("%d no es mayor que %d, vuelve a intoducir el máximo "%(maxim,minim)))
import random
secret=random.randint(minim,maxim)

while not encontrado:
        adivina=input("¿Es %d?"%secret)
        if adivina=="mayor":
            minim=adivina
            secret=random.randint(minim,maxim)
        elif adivina=="menor":
            maxim==adivina
            secret=random.randint(minim,maxim)
        else:
            if adivina=="igual":
                encontrado= True

print ("Tu numero secreto era", secret,". Gracias por jugar conmigo")
    

    




        
