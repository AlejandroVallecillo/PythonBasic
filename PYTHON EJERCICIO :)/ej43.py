def tabla_mult():
    while True:
        num=int(input("INTRODUCE UN NUMERO ENTERO, MIN 1, MAX 20: "))
        if 1<=num<=20:
            break
        else:
            print("ERROR, DEBES DE INTRODUCIR UN ENTERO ENTRE MIN 1, MAX 20")
    x=0
    for _ in range(21):
        res=num*x
        print(f"{num} x {x} = {res}")
        x+=1
tabla_mult()

