#muestra todo los numero pare hasta el 100
lista=[]
for i in range(2,101, 2):
    lista.append(i)
print("LA LISTA DE NUMEROS PARES: ",lista)
listab=[]
for i in range(1,101)[::2]:
    listab.append(i)
print("\nLA LISTA DE NÚMEROS IMPARES: ",listab)