#funcion de bin a decimal, esto se puede usar para octal y hexadecimal, si se hacen algunos retoques
def bin_decimal():
    listax=[]
    listasum=[]
    x=str(input("Introduce el valor en binario: "))
    for i in x:
        listax.append(int(i))
    y=listax[::-1] #si se introduce 100101 devuelve 101001
    for i, valor in enumerate(y):
        mult=valor*(2**i)
        listasum.append(mult)
    print(f"{x} = {sum(listasum)}")
#Este antes no me funcionaba. ahora sí
bin_decimal() 
def bin_decimal_sol2():
    numero = input("Introduce un número binario: ")
    return print(f"El número {numero} en decimal és: {int(numero, 2)}")
bin_decimal_sol2()

