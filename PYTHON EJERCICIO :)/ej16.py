#calcula la longitud de una lista o cadena dada
def longitud():
    print("INTRODUCE NUMEROS, PARA PARAR DE INTRRODUCIR PULSA 0")
    a=True
    lista=[]
    while a:
        x= float(input("INtroduce un valor:"))
        if x==0:
            a=False
        else:
            lista.append(x)
    return len(lista)     
x=longitud() 
print(f"Has introducido {x} carácteres")