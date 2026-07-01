from calculo_promedio import calculo_de_promedio
print("Calculo de promedio")
n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))

promedio_final = calculo_de_promedio(n1,n2,n3)

if promedio_final >= 4.0:
    print("Aprobado")
    print(f"El promedio es : {promedio_final}")
else:
    print("Reprobado")