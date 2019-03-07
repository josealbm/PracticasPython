día=int(input("intoduce el día "))
mes=int(input("intruduce el mes "))
año=int(input("introduce el año "))
bisiesto= año%4

if (día>31) or (día<1) or (mes>12) or (mes<1):
    print("La fecha",día,"/", mes, "/", año, "es incorrecta")

elif (año>2100) or (año<1980):
    print ("La fecha",día,"/", mes, "/", año, "es incorrecta")

elif (día>30) and (mes==2 or mes==4 or mes==6 or mes== 9 or mes== 11):
    print ("La fecha",día,"/", mes, "/", año, "es incorrecta")

elif (día==29) and (mes==2) and (bisiesto!=0):
    print ("La fecha",día,"/", mes, "/", año, "es incorrecta")

else:
    print ("La fecha",día,"/", mes, "/", año, "es correcta")
