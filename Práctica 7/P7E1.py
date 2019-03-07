#Práctica 7 - Ejercicio 1 - José Alberto Martín Marí
#Escribe  un  programa  que  pida  un  texto  por  pantalla,
#este  texto  lo  pase  como  parámetro  a  un 
#procedimiento, y éste lo imprima primero todo en minúsculas y
#luego todo en mayúsculas.

def mayusculas(p):
    print (p.upper())

def minusculas(p):
    print (p.lower())

texto=input("Escribe algo: ")

mayusculas(texto)

minusculas(texto)
