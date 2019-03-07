#Práctica 4 Ejercicio 3 - José Alberto Martín Marí
#Escriu un programa que demani 2 nombres i escrigui la suma de sencers des del primer nombre
#fins al segon.


a=int(input("Escribe el primer número "))
b=int(input("Escribe el segundo número "))
res=0

for i in range(a,b+1):
    res=i+res    

print ("El resultado es", res,)

