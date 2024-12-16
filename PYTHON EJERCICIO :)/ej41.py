#mínim 1 i màxim 900000
def contador_digitos():
    while True:
        num= int(input("Introduce un numero entero, MAYOR QUE 0 y MENOR QUE 1000000: "))
        if 0<num<1000000:
            break
        else:
            print("ERROR, DEBES DE INTRODUCIR UN NUMERO ENTRE ESTAS MEDIDAS (0-1000000)")#[]LOS INCLUYE, ()NO LOS INCLUYE
    m=str(num)
    largo=len(m)
    return largo,num
larga,c= contador_digitos()
print(f"El número {c} tiene {larga} dígitos")