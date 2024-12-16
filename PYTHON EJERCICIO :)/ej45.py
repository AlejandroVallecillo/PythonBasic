def digits_par_impar():
    num=int(input("Introduce un numero: "))
    lista=list(str(num))
    pares=[]
    impares=[]
    for i in lista:
        if int(i) % 2==0:
            pares.append(int(i))
        else:
            impares.append(int(i))
    print(f"Los digitos pares en {num} son: {pares}")
    print(f"Los digitos pares en {num} son: {impares}")
digits_par_impar()