def mostrar_mayores_que(x,list):
    result=[]
    for i in list:
        if i > x:
            result.append(i)
    return result

def craeción_list():
    m=int(input("Cuantos numeros vas a introducir: "))
    list=[]
    for _ in range(m):
        num=int(input("INtroduce un número entero: "))
        list.append(int(num))
    return list

bum= craeción_list()
print("/////////////////////////////////")
x= int(input("\nIntroduce el numero límite: "))
print("/////////////////////////////////")
m= mostrar_mayores_que(x,bum)
print(f"Los números mayores a {x} son {m}")