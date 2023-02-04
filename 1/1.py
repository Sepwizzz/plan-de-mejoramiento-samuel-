def funcion (lista,lista2):
    if(len(lista)>len(lista2)):
        return "lista es mayor"
    elif(len(lista)<len(lista2)):
        return "lista2 es mayor"
    else:
        return "son iguales"
#len dice cuantos elemtos tiene ya sea una palabra o una lista loque uno quiera saber cunatas partes tiene
lista=("hola","como" ,"te","va", "en", "la,vida")
lista2=("bien","y","a","ti")
print(funcion(lista,lista2)) 