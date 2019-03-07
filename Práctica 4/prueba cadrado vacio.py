base=int(input("Dime la base de tu rectángulo "))
altura=int(input("Dime la altura de tu rectángulo "))


for i in range(altura):
        if i == 0 or i == altura-1:
            print(base*'*')
        else: 
            print("*"+" "*(base-2)+"*")   
