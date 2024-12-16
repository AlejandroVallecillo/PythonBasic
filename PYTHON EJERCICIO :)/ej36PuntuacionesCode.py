from operator import itemgetter
def nueva_puntuación(nombre,puntuación):
    with open("ej37Puntuacionesz.txt","a") as file:
        file.write(f"{nombre}:{puntuación}\n")

def devolver_puntuaciones():
    puntuaciones=[]
    with open("ej36Puntuacionesz.txt","r") as file:
        for line in file:
            nombre,puntuación=line.strip().split(":")
            puntuaciones.append([nombre,int(puntuación)])
            puntuaciones.sort(key=itemgetter(1), reverse=True) #ordena las puntuaciones, no se muestra por pantalla
        for x, y in puntuaciones[:10]:
            print(x, "-------->", y)