def mostrar_menu():
    print("Menú")
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
                      
#Opción agregar
#validar nombre
def leer_nombre():
    validar_nombre = False
    while validar_nombre == False:
        nombre_producto = input("Ingrese el nombre del producto: ").strip
        if nombre_producto == "" or nombre_producto == " ":
            print("Error: El nombre del producto no debe de tener espacio y no debe de estar vacío")
        else:
            validar_nombre = True
    return nombre_producto

nombre = leer_nombre()

def leer_precios():
    validar_precios = False
    while validar_precios == False:
        try:
            precio_producto = float(input("Ingrese el precio del producto: "))
            if precio_producto > 0:
                validar_precios = True
            else :
                print("Error: Ingrese un numero decimal mayor a 0")
        except ValueError:
            print("Error: Ingrese un dato numerico decimal")
    return precio_producto

#precio = leer_precios()

def leer_stock():
    validar_stock = False
    while validar_stock == False:
        try:
            stock_producto = int(input("Ingrese la cantidad de stock: "))
            if stock_producto >=0 and stock_producto <= 500:
                validar_stock = True
            else:
                print("Error: Ingrese una cantidad entre 0 y 500")
        except ValueError:
            print("Error: Ingrese un valor numerico entero")
    return stock_producto

stock = leer_stock()

def leer_reposicion():
    reposicion_producto = False
    if stock <= 5 :
        reposicion_producto = True
    else:
        reposicion_producto = False


productos = []
cantidad_disponible_stock = 500
activo = False
while activo == False:
    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 1:
        print("Agregar")
        break
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
        activo = True
