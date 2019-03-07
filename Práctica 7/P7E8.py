#Práctica 7 - Ej 8 - José Alberto Martín
#Escribe un programa que pida una frase, y pase la frase
#como parámetro a una función que debe  
#eliminar los espacios en blanco (compactar la frase).
#El programa principal imprimirá por pantalla 
#el resultado final.

def quitaespacios(p):
    esp=" "
    sin=""
    p=p.replace(esp,sin)
    print (p)

frase=input("Escribe la frase y le quitaré los espacios: ")

quitaespacios(frase)
