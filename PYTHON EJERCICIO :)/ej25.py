#gran lista , introducir elementos, devolver el mayor
def gran_lista():
    lista=[]
    a= True
    print("LISTA 1: PARA FINALIZAR INTRODUCE UN 0")
    while a:
        x=float(input("Introduce elementos: "))
        if x==0:
            a=False
        else:
            lista.append(float(x))
    print(lista)
    print(f"El mayor valor de esta lista es {max(lista)}")
    
gran_lista()