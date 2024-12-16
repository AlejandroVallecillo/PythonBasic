#funcion palabra mas larga, recibe una lista de palbras y devuleve la mas larga
def palabras_mas_largas(Lista):
    if not Lista:  
        return print("La lista está vacía.")
    longitud_maxima = max(len(palabra) for palabra in Lista)
    palabras_largas = [palabra for palabra in Lista if len(palabra) == longitud_maxima]
    return print("La palabra más larga:",{', '.join(palabras_largas)})
def creacion_lista():
    lista = []
    a = True
    print("LISTA 1: PARA FINALIZAR INTRODUCE UN 0")
    while a:
        x = str(input("Introduce elementos: "))
        if x == "0":
            a = False
        else:
            lista.append(x)
    print("Lista:",lista)
    return lista
palabras_mas_largas(creacion_lista()) #cuerpo principal
