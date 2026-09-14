#PARTE A
golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12,"Chitos" , 10]
]
empleados = {1100: "José Alonso", 1200: "Federico Pacheco", 1300: "Nelson Pereira", 1400: "Osvaldo Tejada", 1500: "Gastón Garcia"}
clavesTecnico = ("admin", "CCCDDD", 2020)
golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12,"Chitos" , 10]
]
empleados = {1100: "José Alonso", 1200: "Federico Pacheco", 1300: "Nelson Pereira", 1400: "Osvaldo Tejada", 1500: "Gastón Garcia"}
clavesTecnico = ("admin", "CCCDDD", 2020)
golosinasPedidas = []
eleccion = ""
while eleccion != "d":
    print("="*10, "MÁQUINA DE GOLOSINAS", "="*10)
    print("Menú:")
    print("a. Pedir golosinas.\n"
        "b. Mostrar golosinas.\n"
        "c. Rellenar golosinas.\n"
        "d. Apagar máquina."
        )
    eleccion = input("Elija (a/b/c/d): ").lower()

    if eleccion == "a":
        legajo = int(input("Ingrese su número de legajo: "))
        if legajo in empleados:
            pedido = int(input("Ingrese el código de la golosina que desea: "))
            encontrada = False
            for golosina in golosinas:
                if golosina[0] == pedido:
                    encontrada = True
                    if golosina[2] > 0:
                        golosina[2] -= 1
                        print("¡Disfrute su golosina!")
                        registrada = False
                        for pedida in golosinasPedidas:
                            if pedida[0] == golosina[0]:
                                pedida[2] += 1
                                registrada = True
                                break
                        if not registrada:
                            golosinasPedidas.append([golosina[0], golosina[1], 1])
                    else:
                        print(f"Lo sentimos la golosina {golosina[1]} no se encuentra disponible, seleccione otra golosina o ingresa salir si no desea otra golosina.")
                    break
            if not encontrada:
                print("El código ingresado no existe.")
        else:        
            print("Usted no es empleado de la empresa.")
        pass
    elif eleccion == "b":
        for golosina in golosinas:
            print(f"Código: {golosina[0]} - Nombre: {golosina[1]} - Cantidad: {golosina[2]}")
            
    elif eleccion == "c":
        clave1 = input("Ingrese clave 1:")
        clave2 = input("Ingrese clave 2:")
        try:
            clave3 = int(input("Ingrese clave 3:"))
        except ValueError:
            print("La clave 3 debe ser numérica.")
            clave3 = None
        if clave1 == clavesTecnico[0] and clave2 == clavesTecnico[1] and clave3 == clavesTecnico[2]:
            codigo_golosina = int(input("Ingrese el código de la golosina a recargar"))
            encontrada = False

            for golosina in golosinas:
                if golosina[0] == codigo_golosina:
                    encontrada = True
                    cantidad = int(input("Ingrese la cantidad a recargar: "))
                    if cantidad > 0 :
                        golosina[2] += cantidad
                        print(f"Se recargaron {cantidad} unidades de {golosina[1]}.")
                    else:
                        print("La cantidad debe ser mayor a 0.")
            if not encontrada:
                print("El código ingresado no existe.")
        else:
            print("No tiene permiso de ejecutar la función recarga.")

    elif eleccion == "d":
        total_pedidas = 0
        for pedida in golosinasPedidas:
            print(f"Código: {pedida[0]} - Golosina: {pedida[1]} - Cantidad Pedida: {pedida[2]}")
            total_pedidas += pedida[2]

        print(f"Total de golosinas pedidas: {total_pedidas}")
        print("Apagando la máquina.")

    else:
        print("Opcion no válida. Intente de nuevo.")