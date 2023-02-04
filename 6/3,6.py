def multiplicar(numero):
    for i in range(11):
        resultado=i*numero
        print(numero,"x",i,"=",resultado,)
        
num=int(input("que numero quiere multiplicar"))

multiplicar(num)