#introduce caracter, si es vocal0 VERDADERO
def detector(vocal):
    if vocal in "AEIOUaeiou":
            return print("VERDADERO")
    else:
        return print("FALSO") #AQUÍ HAY FALLO

cov= input("INtroduce un caracter: ")
detector(cov)