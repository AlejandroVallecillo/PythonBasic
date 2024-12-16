#calculadora de numeros enteros y pùnto flotante
import time
def mostrar_opciones():
    print("Calculadora de numeros enteros y punto flotante") #no sé que es punto flotante. de momento solo enteros.
    print("1.Sumar (+)")
    print("2.Restar (-)")
    print("3.Multiplicar (x)")
    print("4.Dividir (/)")
    print("5.OPerar módulo (%)")
    print("6.Cociente entero (//)")
    print("7.Potencia (**)")
    print("8.Función x·10^y")
    print("9.Salir")
    time.sleep(1)
a= True
while a:
    mostrar_opciones()
    sol= int(input("Introduce una opción: "))
    match sol:
        case 1:#+
            num1= int(input("INtroduce el primer entero para la suma: "))
            num2 = int(input("INtroduce el segundo entero para la suma: "))
            res= num1+num2
            print(f"{num1} + {num2} = {res}")
            time.sleep(2)
        case 2:#-
            r1=int(input("INtroduce el primer entero para la resta: "))
            r2=int(input("INtroduce el segundo entero para la resta: "))
            resr= r1 - r2
            print(f"{r1} - {r2} = {resr}")
            time.sleep(2)
        case 3:#x
            m1=int(input("INtroduce el primer entero para la multiplicación: "))
            m2=int(input("INtroduce el segundo entero para la multiplicación: "))
            resm= m1 * m2
            print(f"{m1} x {m2} = {resm}")
            time.sleep(2)
        case 4:#/
            d1=int(input("INtroduce el primer entero para la división: "))
            d2=int(input("INtroduce el segundo entero para la división: "))
            resd= d1/d2
            print(f"{d1} / {d2} = {resd}")
            time.sleep(2)
        case 5: #%
            om1=int(input("INtroduce el primer entero para operar modulo: "))
            om2=int(input("INtroduce el segundo entero para operar modulo: "))
            resom= om1 % om2
            print(f"{om1} % {om2} = {resom}")
            time.sleep(2)
        case 6: #// , queria indicar el resto también, pero mejor no :) 
            ce1=int(input("INtroduce el primer entero para calcular el cociente entero: "))
            ce2=int(input("INtroduce el segundo entero para calcular el cociente entero: "))
            resce= ce1 % ce2
            print(f"{ce1} // {ce2} = {resce}")
            time.sleep(2)
        case 7: #**
            p1=int(input("INtroduce el primer entero para calcular la potencia: "))
            p2=int(input("INtroduce el segundo entero para calcular la potencia: "))
            resp= p1 % p2
            print(f"{p1} // {p2} = {resp}")
            time.sleep(2)
        case 8: #info de como calcular sacada de: puntoflotante.org/formats/fp/
            pf1= float(input("Introduce un coeficiente: "))
            pf2= float(input("Introduce un exponente: "))
            respf= pf1 * (10**pf2)
            print(f"{pf1} x 10^{pf2} = {respf}")
            time.sleep(2)
        case 9:
            print("Has dejado de usar la calculadora")
            time.sleep(1)
            a=False
