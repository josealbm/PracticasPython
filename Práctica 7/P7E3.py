#Práctica 7 -Ej 3 - José Alberto Martín Marí
#Escribe  un  programa  que  lea  una  frase,  y  la  pase  como
#parámetro  a  un  procedimiento,  y  éste 
#debe mostrar la frase con un carácter en cada línea

def partir(p):
    for i in p:
        print (i+"")

frase=input("Escribe una frase: ")

partir(frase)
