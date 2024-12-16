#introducir 2 listas, si alguno de los elmentos de la lista se repite en la otra, mostrar verdadero, sino falso
def superposición(lista, lista2):
    print(f"\nLista 1: {lista}")
    print(f"Lista 2: {lista2}")
    cont=0
    for i in lista:
        if i in lista2:
            cont+=1
        else:
            cont+=0
    if cont!= 0:
        return print("\nSolución: VERDADERO (Se repiten elementos)")
    else:
        return print("\n Solución: FALSO (NO se repiten elementos)")
lista=[]
lista2=[]
a= True
b= True
print("LISTA 1: PARA FINALIZAR INTRODUCE UN 0")
while a:
    x=str(input("Introduce elementos: "))
    if x=="0":
        a=False
    else:
        lista.append(x)
print("LISTA 2: PARA FINALIZAR INTRODUCE UN 0")
while b:
    y=str(input("Inroduce un elemento: "))
    if y=="0":
        b= False
    else:
        lista2.append(y)
superposición(lista, lista2)