# ejercicio Ciclo While_1
print("<1>piedra")
print("<2>papel") 
print("<3>tijera")
eleccion=-1
while eleccion  !=0:
    import random
     
    eleccion= int (input("Ingrese eleccion:"))
    num=random.randint(1,3)

    if eleccion== num:
        print ("Empate", eleccion, "vs", num)
    elif eleccion==1:
        if num==2:
            print ("pierdo", eleccion, "vs", num)
        elif num ==3:
            print ("gano", eleccion, "vs", num)
    elif eleccion==2:
        if num==1:
            print ("gano", eleccion, "vs", num)
        elif num==3:
                print ("pierdo", eleccion, "vs", num)
    elif eleccion==3:
        if num==1:
            print ("pierdo", eleccion, "vs", num)
        elif num==2:
            print ("gano", eleccion, "vs", num)
