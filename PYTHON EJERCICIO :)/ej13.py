import time
def menu_principal():
    op = 0
    while op<1 or op>4:
        print("/////////////////////////////////////////////")
        print("Menú principal")
        print("1. Calculadora d'enters: ")
        print("2. Canvis de base: ")
        print("3. Sortir")
        op = int(input("Selecciona una opció: "))
    return op
def calculadora_enteros():
    print("/////////////////////////////////////////////")
    print("OPCIONES DE CALCULADORA DE ENTEROS")
    print("1.Sumar (+)")
    print("2.Restar (-)")
    print("3.Multiplicar (x)")
    print("4.Dividir (/)")
    print("5.OPerar módulo (%)")
    print("6.Cociente entero (//)")
    print("7.Potencia (**)")
    print("8.Salir")
    x=  int(input("INTRODUCE UNA OPCIÓN: "))
    return x
def suma():
    a=int(input("INtroduce el primer entero: "))
    b= int(input("INtroduce el segundo entero:)"))
    y= a+b
    print(f"{a} + {b} = {y}")
def resta():
    a=int(input("INtroduce el primer entero: "))
    b= int(input("INtroduce el segundo entero:)"))
    y= a-b
    print(f"{a} - {b} = {y}")
def multiplicación():
    a=int(input("INtroduce el primer entero: "))
    b= int(input("INtroduce el segundo entero:)"))
    y= a*b
    print(f"{a} x {b} = {y}")
def división():
    a=int(input("INtroduce el primer entero: "))
    b= int(input("INtroduce el segundo entero:)"))
    y= a/b
    print(f"{a} / {b} = {y}")
def modulo():
    a=int(input("INtroduce el primer entero: "))
    b= int(input("INtroduce el segundo entero:)"))
    y= a%b
    print(f"{a} % {b} = {y}")
def cociente_entero():
    a=int(input("INtroduce el primer entero: "))
    b= int(input("INtroduce el segundo entero:)"))
    y= a//b
    print(f"{a} // {b} = {y}")
def potencia():
    a=int(input("INtroduce el primer entero: "))
    b= int(input("INtroduce el segundo entero:)"))
    y= a**b
    print(f"{a} ^ {b} = {y}")
def cambios_de_base():
    while True:
        print("\nCanvis de Base")
        print("1. Decimal a Binari")
        print("2. Decimal a Octal")
        print("3. Decimal a Hexadecimal")
        print("4. Binari a Decimal")
        print("5. Octal a Decimal")
        print("6. Hexadecimal a Decimal")
        print("7. Tornar al menú principal")
        op = int(input("Selecciona una opció: "))

        if op == 1:
            numero = int(input("Introduce un número decimal: "))
            print(f"El número {numero} en binari és: {bin(numero)[2:]}")
        elif op == 2:
            numero = int(input("Introduce un número decimal: "))
            print(f"El número {numero} en octal és: {oct(numero)[2:]}")
        elif op == 3:
            numero = int(input("Introduce un número decimal: "))
            print(f"El número {numero} en hexadecimal és: {hex(numero)[2:].upper()}")
        elif op == 4:
            numero = input("Introduce un número binari: ")
            print(f"El número {numero} en decimal és: {int(numero, 2)}")
        elif op == 5:
            numero = input("Introduce un número octal: ")
            print(f"El número {numero} en decimal és: {int(numero, 8)}")
        elif op == 6:
            numero = input("Introduce un número hexadecimal: ")
            print(f"El número {numero} en decimal és: {int(numero, 16)}")
        elif op == 7:
            print("Tornant al menú principal...")
            break
        else:
            print("Opció no vàlida.")
        time.sleep(2)

a=  True
while a:
    op=menu_principal()
    match op:
        case 1:
            x= calculadora_enteros()
            match x:
                case 1:
                    suma()
                case 2:
                    resta()
                case 3:
                    multiplicación()
                case 4:
                    división()
                case 5:
                    modulo()
                case 6:
                    cociente_entero()
                case 7:
                    potencia()
                case 8:
                    a=False
        case 2: 
            y= cambios_de_base()
        case 3:
            a=False
            print("Adéu, ha sortit de la calculadora! ")
        case _:
            print("Opció no vàlida")
