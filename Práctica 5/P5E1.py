#Práctica 5 - Ejercicio 1
#Escriu un programa que te demani paraules i les guardi en una llista.
#Per a terminar d'introduir 
#paraules, simplement pitja Enter. El programa termina escribint
#la llista de paraules. 
#Escriu una paraula: viaje
#Escriu més paraules: aventura
#Escriu més paraules: tebeo
#Escriu més paraules: 
#Las paraules que has escrit són ['viaje', 'aventura', 'tebeo'

lista=[]
palabras=input("Escribe una palabra ")

while palabras!="":
    lista.append(palabras)
    palabras=input("Escribe más palabras ")
print ("Las palabras que has escrito son",(lista))
