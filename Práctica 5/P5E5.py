#Práctica 5 - Ejercicio 5 - José Alberto Martín Marí
#Escriu un programa que te demani dos nombres cada vegada més grans i els guardi en una llista.
#Per a terminar d'escriure els nombres, escriu un nombre que no sigui major a l'anterior. El
#programa termina escribint la llista de nombres.
#Escriu un nombre: 6
#Escriu un nombre major que 6: 10
#Escriu un nombre major que 10: 12
#Escriu un nombre major que 12: 25
#Escriu un nombre major que 25: 9
#Els nombres que has escrit són [6, 10, 12, 25] 


numeros=[]
num=int(input("Escribe un número "))
numeros.append(num)
num2=int(input("Escribe número mayor a %d "%(num)))


while num2>=num:
   numeros.append(num2)
   num=num2
   num2=int(input("Escribe otro número mayor a %d "%(num2)))

print ("Los números que has escrito son",(numeros))

