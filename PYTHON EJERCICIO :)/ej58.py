lista= [5,4,3,2,1]
for i in range(len(lista)):
    print(" ".join(map(str, lista))) 
    lista=lista[1:]
