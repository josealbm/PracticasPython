#Práctica 7 - Ej 7 - José Alberto Martín
#Escribe  un  programa  que  lea  una  frase,  y  la  pase  como
#parámetro  a  un  procedimiento.  El procedimiento  contará
#el  número  de  vocales  (de  cada  una)  que  aparecen,
#y  lo  imprimirá  por pantalla. 

def vocales(frase):
    conta=0
    conte=0
    conti=0
    conto=0
    contu=0
    for i in frase:
        if i=="a":
           conta+=1
        elif i=="e":
           conte+=1
        elif i=="i":
           conti+=1
        elif i=="o":
           conto+=1
        elif i=="u":
           contu+=1
    print ("En la frase escrita hay", conta,"aes,", conte,"ees",conti,"íes"
           ,conto,"oes y",contu,"ues")

frase=input("Escribe una frase y te haré un conteo de las vocales que has\n\
utilizado: ")

vocales(frase)
