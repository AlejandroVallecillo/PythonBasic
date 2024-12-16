def crear_lista_ficheros():
    arc = open("ej51z.txt","r")
    lista=[]
    for linea in arc:
        lista.append(linea.split()) #para que agregue más de una fila
    print(lista)
crear_lista_ficheros() #Cuerpo principal
