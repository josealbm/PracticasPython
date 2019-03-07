#Práctica 5 - Ejercicio 7 - José Alberto Martín Marí
#Escriu un programa que demani un nombre (límit) i després et
#demani nombres fins a què la suma
#dels nombres introduits superi un nombre inicial. El programa termina
#escribint la llista de nombres.
#Escriu el límit: 50
#Escriu un valor: 10
#Escriu un altre valor: 25
#Escriu un altre valor: 7
#Escriu un altre valor: 14
#El límit a superar és 50. La llista creada és [10, 25, 7, 14]

lista=[]
limit=int(input("Escribe el límite "))
n=int(input("Escribe un valor "))
i=n

while limit>i:
    lista.append(n)
    n=int(input("Escribe otro valor "))
    i=i+n
lista.append(n)
print ("El límite a superar es", limit,". La lista creada es",lista,)
    
