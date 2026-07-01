def mostrar_menu():
    print("1.Agregar producto")
    print("2.Buscar producto")
    print("3.Eliminar productos")
    print("4.Actualizar estado")
    print("5.Mostrar registros")
    print("6.Salir")

def leer_opcion():
    validar_opt = False
    while validar_opt == False:
        try:
            leer_opt = int(input("Ingrese una opción (1-6): ")) #Cuando esta en gris, significa que no se esta usando
            if leer_opt >= 1 and leer_opt <= 6:
                validar_opt = True
            else:
                print("Error, ingrese nuevamente una opción que este entre 1 y 6 : ")
        except ValueError:
            print("Ha ingresado un dato invalido, debe de ingrear SOLO números enteros")
    return leer_opt #dato que va a devolver el def LEER_OPCION()
                      
opcion = leer_opcion()










productos = []
opcion = 0
if opcion == 1:
    print("Agregar")
elif opcion == 2:
    print("Buscar")
elif opcion == 3:
    print("Eliminar")
elif opcion == 4:
    print("Actualizar estado")
elif opcion == 5:
    print("Mostrar registros")
else: 
    print("Salir")
