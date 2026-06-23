print("calculadora")
print("1.Suma")
print("2.Resta")
opt = int(input("Ingrese una opcion: "))

if opt == 1:
    print("Sumando")
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    resultado = n1+n2
    print(f"El resultado de la suma es : {resultado}")
elif opt == 2:
    print("Restando")
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    resultado = n1-n2
    print(f"El resultado de la resta es : {resultado}")
else:
    print("Opcion invalida")