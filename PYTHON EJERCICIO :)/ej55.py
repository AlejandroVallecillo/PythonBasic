def suma():
    num1=int(input("INTRODUCE EL PRIMER LIMITANTE: "))
    num2=int(input("INTRODUCE EL SEGUNDO LIMITANTE: "))
    res=0
    for i in range(num1,num2+1):
        res=res+i
    return res
print("El resultado es ",suma())