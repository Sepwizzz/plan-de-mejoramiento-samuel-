def maslarga(a,z):
    if (len(a)>len(z)):
        return ("La palabra uno es la mas larga") 
    elif (len (a) < len(z)):
        return ("La palabra dos es la mas larga")
    else:
        return " las palabras son iguales "

disculpa1=("una disculpa por mi mal rendiminto")
disculpa2=("lo sineto por mi bajo rendimiento pero si me gusta programar")

print(maslarga(disculpa1,disculpa2))