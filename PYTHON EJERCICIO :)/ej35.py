#año BISIESTO
def año_de_traspaso(): 
    año=int(input("INtroduce un año: "))
    if año%4==0 and año%100!=0 or año%400==0: #si es un año bisiesto pq debe de de ser divisible entre 400?
        print(f"{año} es un Año de Traspaso")
    else:
        print(f"{año} NO es un Año de Traspaso")

año_de_traspaso()