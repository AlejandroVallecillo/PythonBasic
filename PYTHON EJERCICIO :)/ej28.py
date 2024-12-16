#cadena dada, calcular cuantas mayúsculas hay.
def contar_mayúsculas(texto):
    return sum(1 for i in texto if i.isupper())
texto=input("Introduce un texto: ")
print("En este texto hay:",contar_mayúsculas(texto), "mayúsculas")