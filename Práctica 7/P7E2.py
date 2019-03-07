#Práctica 7 - Ejercicio 2 - José Alberto Martín Marí
#Escribe un programa que lea  el  nombre  y  los  dos  apellidos
#de  una  persona  (en tres  cadenas  de caracteres  diferentes),
#los  pase  como  parámetros  a una  función,  y  ésta  debe  unirlos
#y  devolver una única cadena. La cadena final la imprimirá el programa
#por pantalla.

def unir(a,b,c):
    return print (a+""+b+""+c)

nombre=input("Dime tu nombre: ")
apellido1=input("Dime tu primer apellido: ")
apellido2=input("Dime tu segundo apellido: ")

unir(nombre, apellido1, apellido2)

