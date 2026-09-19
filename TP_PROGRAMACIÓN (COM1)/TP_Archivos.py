#TP ARCHIVOS
#Alumno: Pedro Chávez (Comisión 1)
def cargar_productos(nombre_archivo):
    lista_productos = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            mercaderia = linea.strip().split(",")
            producto = {
                "nombre": mercaderia[0],
                "precio": float(mercaderia[1]),
                "cantidad": int(mercaderia[2])
            }
            lista_productos.append(producto)
    return lista_productos

def guardar_productos(nombre_archivo, lista_productos):
    with open (nombre_archivo, "w") as archivo:
        for producto in lista_productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

def pedir_precio(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("El valor debe ser mayor a 0.")
        except ValueError:
            print("Ingrese un valor numérico.")

def pedir_cantidad(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= 0:
                return valor
            print("La cantidad no puede ser un número negativo.")
        except ValueError:
            print("Solo se admiten números enteros.")

def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip().title()
        if valor == "":
            print("¡ERROR! El campo no puede estar vacío.")
        elif valor.isdigit():
            print("¡ERROR! Este campo no admite números.")
        else:
            return valor

if __name__ == "__main__":
    with open ("productos.txt", "w") as archivo:
        archivo.write("Remera,60000,10\n")
        archivo.write("Pantalon,80000,8\n")
        archivo.write("Zapatilla,120000,5\n")
    stock = cargar_productos("productos.txt")
    print("=== Stock Inicial ===")
    for mercaderia in stock:
        print(f"Producto: {mercaderia['nombre']} - Precio: ${mercaderia['precio']} - En stock: {mercaderia['cantidad']}")

    nombre = pedir_texto("\nIngrese nombre de nuevo producto: ").title()
    precio = pedir_precio(f"Ingrese el precio de {nombre}: ")
    cantidad = pedir_cantidad(f"Ingrese el stock de {nombre}: ")

    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    stock.append(nuevo_producto)
    print("\n=== Stock Actualizado ===")
    for mercaderia in stock:
        print(f"Producto: {mercaderia['nombre']} - Precio: ${mercaderia['precio']} - En stock: {mercaderia['cantidad']}")

    buscado = pedir_texto("\n¿Qué producto desea buscar?: ").strip().title()
    encontrado = False

    for producto in stock:
        if producto["nombre"].title() == buscado:
            print(f"Producto encotrado: {producto['nombre']} - Precio: {producto['precio']} - Stock: {producto['cantidad']}")
            encontrado = True
            break

    if not encontrado:
        print("Ese producto no se encuentra en su stock.")

    guardar_productos("productos.txt", stock)
    print("\nArchivo 'productos.txt' fue actualizado.")
#FIN