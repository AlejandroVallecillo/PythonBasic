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
def esta_ordenada(llista):
    if all(llista[i] <= llista[i+1] for i in range(len(llista)-1)):
        return "Está ordenada de forma ascendente"
    elif all(llista[i] >= llista[i+1] for i in range(len(llista)-1)):
        return "Está ordenada de forma descendente"
    else:
        return "No está ordenada"
lista=crecaión_lista() #Cuerpo principal
print(f"La lista formada es {lista}")
print(esta_ordenada(lista))


