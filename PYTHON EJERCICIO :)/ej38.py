#introduccion de 2 palabras
#si coinciden las tres últimas letras o más = riman mucho
#si solo coinciden las 2 últimas = riman un poco
def Introducción():
    print("------------------------------COMPROBADOR DE RIMA-------------------------------")
    word1=str(input("INTRODUCE LA PALABRA 1: "))
    word2=str(input("INTRODUCE LA PALABRA 2: "))
    return word1, word2
def rimancia(x,y): #separación de elememtos de cada palabra, para su comprobación. e[-1:] para mirar el último caracter 
    x=x.upper()
    y=y.upper()
    if x[-3:] == y[-3:]:
        print("RIMAN MUCHO")
    elif x[-2:] == y[-2:]:
        print("RIMAN UN POCO")
    else:
        print("NO RIMAN UNA MIERDA")
pal1, pal2= Introducción() #Cuerpo principal
rimancia(pal1,pal2)