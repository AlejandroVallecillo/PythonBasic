def crecaión_lista():
    lista= []
    a=True
    print("PARA FINALIZAR CLICA 0")
    while a:
        x=input("Introduce una palabra: ")
        if x!="0":
            lista.append(x)
        else:
            a=False
    print("La lista creada es: ",lista)
    return lista
def elements_parells(lista):
    h=[]
    for i in range(1, len(lista), 2): #si referias a las que se encunetran en "indice par", pon--> range(2,len(lista),2) 
        h.append(lista[i])
    return h
print("Los elementos en posicion par en esta lista, son: ",elements_parells(crecaión_lista()))
