#Práctica 3 - Ejercicio 1 - José Alberto Martín
#Pida al usuario pida al usuarios 5 números y diga cual es el mayor
#y cual el menor.

print ("Escribe cinco números y te diré cuál es el mayor y cuál es el menor")

a=int(input("Por favor introduce el primer número "))
b=int(input("Por favor introduce el segundo número "))
c=int(input("Por favor introduce el tercer número "))
d=int(input("Por favor introduce el cuarto número "))
e=int(input("Por favor introduce el quinto número "))

if a>b and a>c and a>d and a>e:
    print ("El número", a,"es el mayor")
elif b>a and b>c and b>d and b>e:
    print ("El número", b,"es el mayor")
elif c>a and c>b and c>d and c>e:
    print ("El número", c,"es el mayor")
elif d>a and d>b and d>c and d>e:
    print ("El número", d,"es el mayor")
else:
    print ("El número", e,"es el mayor")
