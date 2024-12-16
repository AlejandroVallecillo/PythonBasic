#funcion crear puntos , tome una lista y recree puntos por elemento
def crear_puntos(lista):
    print(lista)
    for i in lista:
        i= int(i)
        print(i* ".")
lista=[]
a= True
print("LISTA 1: PARA FINALIZAR INTRODUCE UN 0")
while a:
    x=str(input("Introduce elementos: "))
    if x=="0":
        a=False
    else:
        lista.append(x)
crear_puntos(lista)
    
