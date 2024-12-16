def nombres_comienzan_a(list):
    result=[]
    for i in list:
        if i[0]== "A" or i[0]=="a":
            result.append(i)
    return result

def creación_lista():
    m=int(input("Cuantos nombres vas a introducir: "))
    list=[]
    for _ in range(m):
        nombre=input("INtroduce un nombre: ")
        list.append(nombre)
    return list

list=creación_lista()
result= nombres_comienzan_a(list)
print(f"La lista de nombre que comienzan por A o a, son: {result}")