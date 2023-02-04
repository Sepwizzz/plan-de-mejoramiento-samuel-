a=int(input("ponga un numero mas de 5 y menos de 10"))
b=int(input("ponga otro numero"))

def funcion (a,b):
    for i in range(a):
        for j in range(b):
            print(i,"-",j)
funcion(a,b)