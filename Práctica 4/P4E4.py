#Práctica 4 Ejercicio 4 - José Alberto Martín Marí
#Escriu un programa que demani un nombre i calculi el seu factorial.


a=int(input("Escribe el número del que quieras hacer el factorial "))
res=1

for i in range(1,a+1):
    res*=i

print ("El factorial de tu número es", res,)
