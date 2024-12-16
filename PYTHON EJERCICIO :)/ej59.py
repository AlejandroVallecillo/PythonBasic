def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def obtener_primos_100():
    primos = [i for i in range(1, 101) if es_primo(i)]
    return primos
primos = obtener_primos_100() #Cuerpo principal
print("Números primos entre 1 y 100:", primos)
print("Cantidad de números primos:", len(primos))
