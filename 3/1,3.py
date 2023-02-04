def funcion(num):
    if num < 10:
        while num<10:
            if num%2!=0:
                print(num)
            num+=1
    elif num > 10:
        while num >10:
            if num%2!=0:
                print(num)
            num-=1
funcion(20)