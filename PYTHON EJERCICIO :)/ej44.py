#sumar digitos, decir si es par o inpar
def suma_digits():
    num=int(input("Introduce un numero: "))
    lista=list(str(num))
    res = sum(int(digit) for digit in lista)
    return res,num
def par_impar(x):
    if x%2==0:
        print(f"{x} es un número par")
    else:
        print(f"{x} es un número impar")

res,num= suma_digits()
print(f"La suma de los digitos de {num} da {res}")
par_impar(res)