def crecaión_lista():
    lista= []
    a=True
    print("PARA FINALIZAR CLICA 0")
    while a:
        x=int(input("Introduce un numero: "))
        if x!=0:
            lista.append(x)
        else:
            a=False
    return lista
def hay_duplicados(lista):
    if len(lista) != len(set(lista)): #si hay agun dupliacado en la lista, el set reducirá la longitud. [1,2,3,4,4]-->set-->[1,2,3,4]
        return "Hay duplicados"
    else:
        return "No hay duplicados"
lista= crecaión_lista() #cuerpo principal
print(hay_duplicados(lista))


