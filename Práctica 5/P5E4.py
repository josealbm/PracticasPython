#Práctica 5 - Ejercicio 4 - José Alberto Martín Marí
#Escriu un programa que te demani dos nombres, de manera que el segon sigui major que el
#primer. El programa termina escrivint els dos nombre tal i com es demana.
#Escriu un nombre: 6
#Escriu un nombre major que 6: 6
#6 no és major que 6. Torna a ficar un nombre: 1
#1 no és major que 6. Torna a ficar un nombre: 8
#Els nombres que has escrit són 6 i 8.

num1=int(input("Escribe un número "))
num2=int(input("Escribe un número mayor que %d "%(num1)))

while num2<=num1:
    print (num2,"no es mayor que",num1,)
    num2=int(input("Vuelve a introducir un número mayor que %d "%(num1)))

print ("Los números que has escrito son",num1,"y",num2)
