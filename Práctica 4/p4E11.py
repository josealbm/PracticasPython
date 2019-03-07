#Práctica 4 ejercicio 11 - José Alberto Martín Marí
#Escriu un programa que demani un nombre i retorni els seus divisors.
#Dona'm un nombre:
#200
#Els divisors 200 són 1 2 4 5 8 10 20 25 40 50 100 200
#Adéu!

n=int(input("Dame un número "))

for i in range(1,n):
    if n%i==0:
        print ("El número", i,"es divisor de", n,)
print ("Adiós, gracias!")
