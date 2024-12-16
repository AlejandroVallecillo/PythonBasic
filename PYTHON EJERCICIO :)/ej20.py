# palindromo() falso o vedadero, palabras que se escriben igual de izquierda a derecha
def palindromo():
    palabra= input("Introduce una palabra: ")
    palabra= palabra.split()
    for i in palabra:
        i=i.lower()
        if len(i) >= 3 and i==i[::-1]: #len(i)>= 3, para evitar que el usuario introduzca solo una letra
            print("VERDADERO")
        else:
            print("FALSO")
palindromo()