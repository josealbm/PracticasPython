#Práctica 6 - Ejercicio 2 - José Alberto Martín Marí
#Escribe un programa que permita crear una lista de palabras y que,
#a continuación, pida una palabra y diga cuántas veces aparece esa
#palabra en la lista. 

lista=[]
palabras=int(input("Dime cuántas palabras va a tener tu lista "))

for i in range(palabras):
    palabra=input("Dime la palabra %d: "%(i+1))
    lista.append(palabra)

print ("La lista creada es: ", lista,)
pal=input("Dime la palabra que quieras saber cuántas veces está en la lista: ")
print ("La palabra",pal,"aparece",lista.count(pal),"veces")
