def eliminar_capua():
    lista= []
    a=True
    print("PARA FINALIZAR CLICA 0")
    while a:
        x=input("Introduce algo: ")
        if x!="0":
            lista.append(x)
        else:
            a=False
    mista=lista[1:-1]
    print(f"La lista inicial era {lista}")
    print(f"La nueva lista es {mista}")
eliminar_capua()