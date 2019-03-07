#Práctica 5 - Ejercicio 6 - José Alberto Martín Marí
#Escriu un programa que demani primer dos nombres (màxim i mínim)
#i que després te demani 2 nombres  situats  entre  ells.
#Per  a  terminar  d'escriure  nombres,  escriu  un  nombre  que  no  sigui 
#comprès entre els dos valors inicials. El programa 
#termina escribint la llista de nombres.
#Escriu un nombre: 6
#Escriu un nombre major que 6: 4
#4 no és major que 6. Torna-ho a probar: 50
#Escriu un nombre entre 6 i 50: 45
#Escriu un altre nombre entre 6 i 50: 13
#Escriu un altre nombre entre 6 i 50: 4
#Els nombres situats entre 6 i 50 que has escrit són [45, 13]

numeros=[]
num=int(input("Escribe un número "))
num2=int(input("Escribe número mayor a %d "%(num)))
while num2<=num:
    num2=int(input("%d no es mayor que %d. Vuelve a probar "%(num2,num)))
num3=int(input("Escribe un número que esté entre %d y %d "%(num,num2)))
while num3>=num and num3<=num2:
    numeros.append(num3)
    num3=int(input("Escribe otro número que esté entre %d y %d "%(num,num2)))
    

print ("Los números situados entre %d y %d que has escrito son "%(num,num2),(numeros))

