
def funcion( tabla,div):
    for i in range(11):
        if (tabla>=0):
            print(tabla,"x",i,"=",i*tabla)
        else:
            print("no se puede es una tabla de multiplicar")
tabla=int(input("ponga un numero para la tabla de multiplicar "))
funcion(tabla,10)

