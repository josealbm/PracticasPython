#Práctica 5 - Ejercicio 2 - José Alberto Martín
#Escriu un programa que te demani nombres i els guar
#di en una llista. Per a terminar d'introduir 
#nombres, simplement pitja Enter. El programa termin
#a escrivint la llista de nombres. 
#Escriu un nombre:
# 14
#Escriu un altre nombre:
# 123
#Escriu un altre nombre:
# -25
#Escriu un altre nombre:
# 123
#Escriu un altre nombre: 
#Els nombres que has escrit són [14, 123, -25, 123] 

lista=[]
numeros=input("Escribe un número ")

while numeros!="":
    lista.append(numeros)
    numeros=input("Escribe otro número ")

print ("Los números que has escrito son",(lista),)
