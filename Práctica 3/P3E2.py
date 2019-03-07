#Práctica 3 - Ejercicio 2 - José Alberto Martín
#Pida al usuario 5 números y diga si estos estaban en
#orden decreciente, creciente o desordenados.

print ("Escribe cinco números y te diré que orden has utilizado")

a=int(input("Escribe el primer número "))
b=int(input("Escribe el segundo número "))
c=int(input("Escribe el tercer número "))
d=int(input("Escribe el cuarto número "))
e=int(input("Escribe el quinto número "))

if a>b and b>c and c>d and d>e:
    print ("Has escrito tus números en orden decreciente")
elif a<b and b<c and c<d and d<e:
    print ("Has escrito tus números en orden creciente")
else:
    print ("Has escrito los números desordenados")
