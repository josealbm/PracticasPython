#Práctica 5 - Ejercicio 8 - José Alberto Martín Marí
#Escriu un programa que et demani primer un nombre i després et demani nombres
#fins a què la suma dels nombres introduïts coincideixi amb el nombre inicial.
#El programa termina escribint la llista de nombres.
#Escriu el límit: 50
#Escriu un valor: 10
#Escriu un altre valor: 45
#45 és massa gran. Escriu un altre valor: 1
#Escriu un altre valor: 39
#El límit a alcançar és 50. La llista creada és [10, 1, 39]

lista=[]
limit=int(input("Escribe el límite "))
n=int(input("Escribe un valor "))
i=n

while limit>i:
    lista.append(n)
    n=int(input("Escribe un valor "))
    while(i+n)>limit:
        n=int(input("%d es demasiado grande, escribe otro valor "%(n)))
    i+=n
lista.append(n)

    
print ("El límite a alcanzar es", limit,". La lista creada es",lista,)
