def pvtada_historica():
    while True:
        num=int(input("Introduce un número entero, MENOR A 100: "))
        if 0<num<100:
            break
        else: 
            print("ERROR, DEBES INTRODUCIR UN NUMERO ENTERO MENOR A 100 Y MAYOR A 0")
    res=0
    x=num
    while True:
        num=num-4
        if num <= 0:
            break
        else:
            res=(num**2)+res
    return res,x

Solución,numero=pvtada_historica()
print(f"Tras introducir {numero} la operación nos ha dado {Solución}")
        