#Práctica 3 - Ejercicio 3 - José Alberto Martín
#Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, y pida los
#datos según que caso y muestre el resultado.

figgeo=input("Dime si prefieres calcular el área de un cuadrado o un triángulo ")

if figgeo==("cuadrado"):
    lado=int(input("Dime el lado de tu cuadrado "))
    áreacua=lado**2
    print ("El área de tu cuadrado es", áreacua)

else:
    base=int(input("Dime la base del triángulo "))
    alt=int(input("Dime la altura del triángulo "))
    áreatri=(base*alt)/2
    print ("El área de tu triángulo es", áreatri)
    
        
                
