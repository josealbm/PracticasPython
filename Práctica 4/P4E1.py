#Práctica 4 Ejercicio 1 - José Alberto Martín
#Escriu un programa que escrigui els següents nombres (la separació entre nombre és per a
#facilitar-te sabre quants de nombres s'ha d'escriure en cada bucle) i en el que la funció range que
#utilitzis tengui un únic argument (per exemple, per a la primera llista range(10)).

bucle=int(input("Dime que bucle prefieres ver: el 1, el 2, el 3, el 4, o el 5 "))

if bucle==1:
    for i in range(10):
        print (i+1)
elif bucle==2:
    for i in range(10):
        print ((i+1)*2)
elif bucle==3:
    for i in range(10):
        print ((i+10)*2)
elif bucle==4:
    for i in range(6):
        print ((i*4)+10)
elif bucle==5:
    for i in range(9):
        print ((i+40)-(i*6))
