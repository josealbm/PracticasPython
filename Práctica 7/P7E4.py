#Práctica 7 -Ej 4 - José Alberto Martín Marí
#Escribe un programa que pida una frase, y le pase como parámetro
#a una función dicha frase. La función  debe  sustituir  todos
#los  espacios  en  blanco  de  una  frase  por  un  asterisco,
#y  devolver  el resultado para que el programa principal la imprima
#por pantalla. 

def asterisco(p):
    b=" "
    c="*"
    print (p.replace(b,c))

frase=input("Escribe una frase ")

asterisco(frase)
