#index palabra, segun una lista creada, buscar un palabra, si esta se encuentra en la lista, marcar donde se encuentar, sino indicra -1
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
    return lista
def index_palabra(lista):
    palabra=input("Introduce que palabra buscas bien escrita: ")
    if palabra in lista:
        return lista.index(palabra)
    else:
        return "-1, Es decir, no se encuentra en la lista, o no está bien escrita"
print("La palabra que buescas se encunetra en el indice: ",index_palabra(crecaión_lista()))