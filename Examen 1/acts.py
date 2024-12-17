import random
#ejercicio1
def leer_lista_enteros():
    print("PARA TERMINAR PULSA . ")
    lista=[]
    x="a"
    while x!=".": #Soy de usar un 0 en vez de un punto :(
        x=input("Introduce un numero entero: ")
        if x!=".":
            lista.append(int(x))
    return lista
 #ej2
def lista_impares(lista):
    filtro=filter(lambda x: x%2!=0,lista)
    filtro=list(filtro)
    return filtro
#ej3
def lista_sumar_pares(lista):
    filtro=filter(lambda x: x%2==0,lista)
    filtro=list(filtro)
    x=sum(filtro)
    return x
#ej4
def buscar_num_lista(lista,num):
    res=[]
    if num not in lista:
        return print("No se encuentra en la lista")
    else:
        for i in range(len(lista)):
            if lista[i]==num:
                res.append(i+1)
    if len(res)==1:
        return print(f"El numero {num} se encuentra en la posición {res}")
    elif len(res)>1:
        return print(f"El numero {num} se encunetra en las posiciones: {res}")
#ej5 
def leer_lista_palabras():
    print("PARA TERMINAR PULSA . ")
    lista=[]
    x="a"
    while x!=".":
        x=str(input("Introduce una palabra: "))
        if x!=".":
            lista.append(x)
    return lista
#ej6
def crear_palabra_lista(lista):
    res=[]
    for i in lista:
        res.append(i[0])
    res = ''.join(res) #No me acordaba del .join X.X
    return print(res)
#ej7
def crear_lista_num_aleatorio():
    lista=[]
    for i in range(5):
        x=random.randint(1,101)
        lista.append(x)
    return lista
#ej8
def comparar_listas(l1, l2):
    res=[]
    for i in range(5): #imaginación
        if l1[i] in l2 and l1[i]==l2[i]:
            res.append(2)
        elif l1[i]!=l2[i] and l1[i] in l2:
            res.append(1)
        elif l1[i] not in l2:
            res.append(0)
    return res
#ej9
def mayores_edad(edad1, edad2):
    if edad1 >=18 and edad2>= 18:
        return print("Ambos son mayores de edad")
    elif edad1>=18 and edad2<18:
        return print(f"{edad1} es mayor y {edad2} es menor de edad")
    elif edad1<18 and edad2>=18:
        return print(f"{edad1} es menor y {edad2} es mayor de edad")
    elif edad1<18 and edad2<18:
        return print("Ambos son menores de edad")
#ej10
def menu():
    print("(1) Leer lista enteros")
    print("(2) Lista impares")
    print("(3) Lista sumar pares")
    print("(4) Buscar numero en la lista")
    print("(5) Leer lista palabras")
    print("(6) Crear lista mediante iniciales")
    print("(7) Crear lista numeros aleatorios")
    print("(8) Comparación de listas")
    print("(9) Mayores de edad")
    while True:
        op=int(input("Introduce una opción: "))
        if 1<=op<=9:
            break
        else:
            print("ERROR, debes de escoger una de estas opciones")
    match op:
        case 1:
            return print("LISTA: ",leer_lista_enteros())
        case 2:
            return print("lista de impares: ",lista_impares(leer_lista_enteros()))
        case 3:
            return print("LA SUMA DE LOS NUMEROS PARES ES: ",lista_sumar_pares(leer_lista_enteros()))
        case 4:
            x=leer_lista_enteros()
            n=int(input("Introduce el numero que deseas buscar: "))
            return buscar_num_lista(x,n)
        case 5:
            return print("LISTA: ",leer_lista_palabras())
        case 6:
            return print("Palabra creada: ",crear_palabra_lista(leer_lista_palabras()))
        case 7:
            x=crear_lista_num_aleatorio()
            return print(f"La lista formada aleatoriamente es: {x}")
        case 8:
            x=[1,2,3,4,5]
            y=[1,3,4,4,0]
            print("L1: ",x, "L2: ",y)
            return print("Comparación: ",comparar_listas(x,y))
        case 9:
            uno= int(input("Introduce la primera edad: "))
            dos= int(input("Introduce la segunda edad: "))
            return mayores_edad(uno, dos)
    
menu() #cuerpo principal
#En conclusión, eran buenas ideas, pero con ligeros fallos ;)