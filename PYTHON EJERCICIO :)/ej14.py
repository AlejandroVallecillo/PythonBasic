#Calculadora que recibe 2 numeros y devuelve el mayor
def gran(x,y):
    if x > y:
        return print(f"El numero mas grande es: {x}")
    if x < y:
        return print(f"El numero mas grande es: {y}")
    if x==y:
        return print("Ambos son el mismo nuemro iguales")
    
m= float(input("Introduce el primer valor: "))
n= float(input("INtroduce el segundo valor: "))
gran(m,n)