#Práctica 6 - Ejercicio 10 - José Alberto Martín Marí
#Escribe un programa que pida un número y a continuación
#escriba la lista de todos los divisores 
#del número (incluidos el uno y él mismo).

divisores=[]
num=int(input("Dime un número: "))
numdivisores=0

for i in range(1,num+1):
    if num%i==0:
        divisores.append(i)
        numdivisores+=1

print (num,"tiene", numdivisores,"divisores: ", divisores)
    
