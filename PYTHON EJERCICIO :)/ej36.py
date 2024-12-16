#modificar Este actividad, para contar puntos, y mostar lista de puntuaciones
#Puedo hcer un while global, que comience en true, y en caso que no quiere inroducir otro jugador 
#O puedo incuir un marcador/ pagina de texto a parte, donde se hayan los nombres de los jugadores y su puntuación. copiar del otro pc
#/////////////////////////////
import ej36PuntuacionesCode
import random
import time


# Funció on expliquem què passa
def intro():
    print ("""En una època on els gegants governen Menorca. Nosaltres necessitem menjar,
    Estem seguint el rastre de l'olor del menjar, però ens trobem en una cruïa.
    Al final de cada camí hi ha un talaiot, en un viuen els gegants bons que ens convidaran
    i en l'altre són uns caníbals afamats, i ens menjaran just ens vegin.
    """)

# Funció on demanem a quin talaiot volem anar
def canviTalaiot():
    talaiot = ""
    while talaiot != "1" and talaiot != "2":
        talaiot = input("A quin Talaiot vols anar? Introdueixi 1 o 2: ")
    return talaiot

# Funció que ens indica si compartiran el menjar o serem nosaltres el seu àpat
def trobada(canviTalaiot,puntos):#Agrego los puntos/////////////
    print ("T'estas apropant al talaiot...")
    time.sleep(2)
    print ("Està fosc i és tenebrós...")
    time.sleep(2)
    print ("Un gran gegant salta davant teu, t'agafa i ...")
    print ("")
    time.sleep(2)
    gegantamic = random.randint (1, 2)
    if canviTalaiot == str(gegantamic):
        print ("Et convida a menjar...")
        puntos+=1 #si acierta agrega puntos/////////
        print("--------------------HAS CONSEGUIDO UN PUNTO----------------------") #estas 2 lineas son adicionales, para que el jugador sepa cunado gana un punto, y cuantos lleva
        print(f"EL MARCADOR DE PUNTOS ES {puntos}") 
    else:
        print ("Se't menja d'un mos...ÑAMÑAMÑAM")
        print(f"\nEL MARCADOR DE PUNTOS ES {puntos}")
    return puntos

# Funció principal // Teacher no es a malas, pero que coñazo de juego, esperar 6 segundo una o dos veces, ok, pero más de eso, es jodido
puntos=0
nombre=input("INTRODUCE TU NOMBRE: ")
partidaNova = ("si")
while partidaNova == ("s") or partidaNova == ("si"):
    intro()
    nTalaiot = canviTalaiot()
    puntos=trobada(nTalaiot,puntos) #creación  de puntuación, evita que la puntuación se reinicie
    partidaNova = input("Vols tornar a mejar (jugar)? Introdueixi si o no: ")
    print("\n")
print("Ha terminado el juego")
print(f"EL JUGADOR {nombre} HA LOGRADO UNA PUNTUACIÓN DE {puntos}")
ej36PuntuacionesCode.nueva_puntuación(nombre,puntos)
print("\nLAS 10 MEJORES PUNTUACIONES SON: ")
ej36PuntuacionesCode.devolver_puntuaciones()

