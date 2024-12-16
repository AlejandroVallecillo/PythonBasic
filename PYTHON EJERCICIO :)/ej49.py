import random
def lista_20():
    lista=[]
    for i in range(20): #si pones 6 en vez de 20-- se ve claramente que funciona
        i=random.randint(1,101) #si pones 20 en vez de 101-- se ve claramente que funciona
        lista.append(i)
    return lista
def hay_duplicados(lista):
    if len(lista) != len(set(lista)): #si hay agun dupliacado en la lista, el set reducirá la longitud. [1,2,3,4,4]-->set-->[1,2,3,4]
        return "Hay duplicados"
    else:
        return "No hay duplicados"
lista=lista_20()
print(lista)
print(hay_duplicados(lista))