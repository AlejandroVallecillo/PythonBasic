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
    print("La lista formada es: ",lista)
    return lista
def eliminar_dupliacdos(lista):
    return set(lista)
print("La lista sin duplicados es: ", eliminar_dupliacdos(crecaión_lista())) #CUERPO PRINCIPAL
