#Práctica 7 - Ej 9 - José Alberto Martín
#Escribe un programa que pida dos palabras las pase 
#como parámetro a un procedimiento y diga si 
#riman o no. Si coinciden las tres últimas letras tiene
#que decir que riman. Si coinciden sólo las dos 
#últimas tiene que decir que riman un poco y si no, 
#que no riman.

def poeta(a,b):
    if a[-1]==b[-1] and a[-2]==b[-2] and a[-3]==b[-3]:
       print ("Eres todo un poeta, tus palabras riman")
    elif a[-1]==b[-1] and a[-2]==b[-2]:
       print ("Casi lo tienes, tus palabras riman un poco")
    else:
       print ("Lo siento, tus palabras no riman")

palabra1=input("Escribe una palabra: ")
palabra2=input("Escribe otra palabra: ")

poeta(palabra1,palabra2)
