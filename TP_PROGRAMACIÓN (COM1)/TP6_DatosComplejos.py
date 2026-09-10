#TP 6 - ESTRUCTURAS DE DATOS COMPLEJOS
#ALUMNO: PEDRO CHAVEZ (COMISION 1)

#ACTIVIDAD 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)
print("=" * 20)

#ACTIVIDAD 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)
print("=" * 20)

#ACTIVIDAD 3
frutas = list(precios_frutas.keys())
print(frutas)
print("=" * 20)

#ACTIVIDAD 4
agenda = {}
for i in range(5):
    nombre = input("Nombre del contacto: ")
    numero = int(input("Número: "))
    agenda[nombre] = numero

consulta = input("Consultar contacto: ")
if consulta in agenda:
    print(agenda[consulta])
else:
    print("El contacto no está en su agenda.")
print("=" * 20)

#ACTIVIDAD 5
frase = input("Ingrese una frase: ")
palabras = frase.lower().split()
palabras_unicas = set(palabras)
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
print("Palabras únicas:", palabras_unicas)
print("Recuento de palabras:", recuento)
print("=" * 20)

#ACTIVIDAD 6
alumnos = {}
for i in range(3):
    nombre = input("Nombre: ")
    notas = []

    for j in range(3):
        nota = float(input(f"Nota {j + 1}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)
    print(" " * 20)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")
print("=" * 20)

#ACTIVIDAD 7
parcial1 = {"Ana", "Juana", "Mateo", "Leo", "Sonia"}
parcial2 = {"Sonia", "Brenda", "Mateo", "Lupe", "Leo"}

aprobados_1y2 = parcial1.intersection(parcial2)
aprobados_1o2 = parcial1 ^ parcial2
aprobados = parcial1.union(parcial2)
print(f"Alumnos que aprobaron ambos parciales: {aprobados_1y2}")
print(f"Alumnos que aprobaron solo uno de los parciales: {aprobados_1o2}")
print(f"Lista total de aprobados (al menos uno): {aprobados}")
print("=" * 20)

#ACTIVIDAD 8
productos = {'Chocolates': 5, 'Gaseosas': 5, 'Galletas': 20, 'Facturas': 15}
producto = input("Consulte stock de producto: ").title()

if producto in productos:
    print(f"Stock actual de {producto}: {productos[producto]}")
    agregado = int(input("Ingrese las unidades que desea agregar al stock: "))
    productos[producto] += agregado
else:
    print("No cuenta con ese producto.")
    ingreso_stock = int(input(f"Ingrese stock para {producto}: "))
    productos[producto] = ingreso_stock
print(f"Stock actualizado: {productos}")
print("=" * 20)

#ACTIVIDAD 9
calendario = {
    ("lunes", "08:00"): "Clase de Org. Empresarial",
    ("martes", "08:00"): "Clase de Programación 1.",
    ("miércoles", "08:00"): "Clase de AySO.",
    ("jueves", "09:00"): "Clase de Org. Empresarial",
    ("viernes", "10:30"): "Consulta médica.",
    ("sábado", "13:00"): "Almuerzo familiar.",
    ("domingo", "18:30"): "Función de cine."
}
dia = input("Qué día quiere consultar: ").lower()
hora = (input("Qué horario (HH:MM): "))
busca = (dia, hora)
if busca in calendario:
    print(f"Su evento del día {dia} a las {hora} es: {calendario[busca]}")
else:
    print("No hay eventos programados para ese día y hora.")
print("=" * 20)

#ACTIVIDAD 10
original = {"Argentina": "Buenos Aires",
            "Perú": "Lima",
            "España": "Madrid",
            "EE. UU.": "Washington D.C."
            }
print(f"Lista original: {original}")
invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais
print(f"Lista invertida: {invertido}")
print("=" * 20)
#FIN