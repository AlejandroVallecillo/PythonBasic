#filtar palabras(), recibe una lista y x, devuele las palabras con mas de x caracteres
def filtrar_palabras(lista):
    xwords= []
    x=int(input("Introduce un valor minimo: "))
    for i in lista:
        if len(i) > x:
            xwords.append(i)
    print(f"Las palabras con mas acracteres que {x} son: {xwords}")

lista=[]
a= True
print("LISTA 1: PARA FINALIZAR INTRODUCE UN 0")
while a:
    x=str(input("Introduce elementos: "))
    if x=="0":
        a=False
    else:
        lista.append(x)  #se crea la lista a introducir, todo será tomado como texto
filtrar_palabras(lista)
