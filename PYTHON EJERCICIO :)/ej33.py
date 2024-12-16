def nombres_comienzan_por(list):
    result=[]
    n=str(input("Introduce la letra de filtraje: ")).lower()
    for i in list:
        if i[0].lower()== n:
            result.append(i)
    return result, n

def creación_lista():
    m=int(input("Cuantos nombres vas a introducir: "))
    list=[]
    for _ in range(m):
        nombre=input("INtroduce un nombre: ")
        list.append(nombre)
    return list

list=creación_lista()
result, n= nombres_comienzan_por(list)
print(f"La lista de nombre que comienzan por {n}, son: {result}")