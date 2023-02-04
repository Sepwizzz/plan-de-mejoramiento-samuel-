def fun():
    jugador={"mesi":["nace en 1987","de argentina"],"cristiano":["nace1987","de portugal"]}
    a=input("ponga un jugador de futbol:")
    for i in jugador:
        print(i,"\n---------")
    if a == "mesi":
            print("mesi ya se retira este año ",jugador[a])
    elif a =="cristiano":
        print(" el mejor del mundo ",jugador[a])    
fun()