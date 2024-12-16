#Calculo de capital, usuario de be de introducir: 
#Cantidad a solicitar (50.000-800.000€), interes (0,5%-13%), años(3-40)
#c.inicial*(1+interes/100)**años= €
def introducción_datos(): #sin correccion de errores
    while True:
        c_inicial=float(input("INTRODUCE TU CAPITAL INICIAL (ENTRE 50000 Y 800000): "))
        if 50000 <= c_inicial <= 800000:
            break
        else: 
            print("DEBES DE INTRODUCIR UNA CANTIDAD ENTRE 50000 Y 800000")
    while True:
        interés=float(input("\nINTROUCE EL PORCENTAJE DE INTERÉS SIN % (ENTRE 0.5 Y 13): "))
        if 0.5<= interés <=13:
            break
        else:
            print("DEBES DE INTRODUCIR UN INTERÉS ENTRE 0.5 Y 13%")
    while True:
        años=int(input("\nDURANTE CUANTOS AÑOS (ENTRE 3 Y 40): "))
        if 3<= años <= 40:
            break
        else:
            print("DEBES DE INTRODUCIR UNA CANTIDAD DE AÑOS ENNTRE 3 Y 40")
    calculo=c_inicial*(1+interés/100)**años
    print("Tú capital final es de ",round(calculo,2),"€")
introducción_datos()#Cuerpo principal