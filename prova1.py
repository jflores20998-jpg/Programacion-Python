def menu():
    opcio = 0
    while (opcio < 1 or opcio > 4):
        print("""
        Menu principal:
        1. suma
        2. Resta
        3. Multiplicacio
        4. Divisio
        """)
        opcio = int (input("indiui el nuemro de la funcio que va a ejecutar:"))
    return opcio 

#programa principal 

op =menu()
match(op):
    case 1:
        print("operaciones de Suma: \n ")
        X =int(input("introduce el primer num:"))
        Y =int(input("introduce el segundo num:"))
        print("la suma de {} i {} es {}".format(X, Y, X+Y))
    case 2:
        print("operacio de Resta \n ")
        X=int(input("introduce el primer num:"))
        Y=int(input("introduce el segundo numero:"))
        print("la resta de {} i {} es {}".format(X, Y, X-Y))
    case 3:
        print("operaciones de Multiplicaion \n ")
        X=int(input("introduce el primer num:"))
        Y=int(input("introduce el segundo num:"))
        print("la multiplicacio de {} i {} es {}".format(X, Y, X*Y))
    case 4: 
        print("operaciones de divisio \n ")
        X=int(input("introduce el primer num:"))
        Y=int(input("introduce el segundo num:"))
        print("la divisio de {} i {} es {}".format(X, Y, X/Y))
    case _:
        print("en cualquier otro caso")
