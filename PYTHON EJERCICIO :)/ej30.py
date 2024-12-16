#año actual, año nacimiento , nombre ... Muestre años que cumplirá
#puedo hacern diccionario que incluya 4 listas
#he de realizar una funcion que pida introducir todos los datos, este los dibvidira por 3 listas en un diccionario{(nombres)(f.nacimientos)(cumplirán)}
#hacer un detector, es decir si me introducin un fecha anterior a su nacimiento, cambiar la variable por "Aún no has nacido"
año_actual= int(input("INtroduce el año actual: "))
print("////////////////////////////////////////////////////")
def recolección_datos():
    lista_nombres=[]
    lista_nacimientos=[]
    lista_años_finales=[]
    for _ in range(4):
        año_nacimiento= int(input("Introduce tu año de nacimiento: ")) 
        lista_nacimientos.append(año_nacimiento)
        nombre= input("Introduce tu nombre: ")
        print("////////////////////////////////////////////////////")
        lista_nombres.append(nombre)
        años_final= año_actual-año_nacimiento
        if años_final < 0:
            años_final=0
            lista_años_finales.append(años_final)
        else:
            lista_años_finales.append(años_final)
    return lista_nombres, lista_nacimientos, lista_años_finales
lnombres, lnacimientos, lañosf= recolección_datos()

print(lnombres, lnacimientos, lañosf)

print("{:<20} {:<20} {:<20}".format("Nombre","Fecha de Nacimiento", "Años que cumplirá"))
q=0
for _ in range(2):
    print("{:<20} {:<20} {:<20}".format(lnombres[q],lnacimientos[q], lañosf[q]))
    #print(f"{lnombres[q]}            {lnacimientos[q]}                  {lañosf[q]}") #se debe de mostrar esto con cada nombre
    q+=1
