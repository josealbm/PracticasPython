#Práctica 5 - Ejercicio 3  - José Alberto Martín Marí
#Escriu un programa que demani notes i les guardi en una llista. Per a terminar d'introduir notes,
#escriu una nota que no estigui entre 0 i 10. El programa termina escrivint la llista de notes.
#Escriu una nota: 7.5
#Escriu una nota: 0
#Escriu una nota: 10
#Escriu una nota: -1
#Las notas que has escrit són [7.5, 0.0, 10.0]

notas=[]
nota=float(input("Escribe una nota "))

while nota>=0 and nota<=10:
    notas.append(nota)
    nota=float(input("Escribe una nota "))
print ("Las notas que has escrito son",(notas))
