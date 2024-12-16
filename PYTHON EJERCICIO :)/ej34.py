def contar_vocales():
    pa= str(input("Introduce una palabr: ")).lower()
    a=0
    e=0
    i=0
    o=0
    u=0
    for k in pa:
        if k == "a":
            a+=1
        elif k == "e":
            e+=1
        elif k == "o":
            o+=1
        elif k == "i":
            i+=1
        elif k== "u":
            u+=1
    print(f"Hay {a} a's // {e} e's // {i} i's // {o} o's // {u} u's")

contar_vocales()