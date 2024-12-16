#sumar componentes de una lista y multilpicar tambien
a =True 
lista= []
print("INTRODUCE NUMEROS, PARA DEJAR DE INTRODUCIR PULSA 0")
while a:
    x= int(input("INTRODUCE UN NUMERO ENTERO: "))
    if x==0:
        a=False
    else:
        lista.append(x)
y=sum(lista)
print(f"La suma de los componentes de la lista {lista} es: {y}")
