# recibe 3 numero y muestra el mayor
def gran_de_tres(x,y,z):
    if x> y and x> z:
        return print(f"El numero mas rande es {x}" )
    elif y > x and y > z:
        return print(f"El numero mas rande es {y}")
    elif z > y and z > x:
        return print(f"El numero mas grande es {z}")
    elif z == y == x:
        return print("Todos son el mismo numero")
    
m= float(input("Introduceel primer valor: "))
n= float(input("Introduceel segundo valor: "))
o= float(input("Introduceel tercer valor: "))
gran_de_tres(m,n,o) 

