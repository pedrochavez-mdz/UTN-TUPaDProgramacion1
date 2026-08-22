# TRABAJO PRACTICO 1: Estructuras Secuenciales.
# ALUMNO: PEDRO CHÁVEZ

# Actividad 1: Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# Actividad 2: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
nombre = input("Ingresa tu nombre: ")
print(f"Hola, {nombre}!")

# Actividad 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
nombre = input("Ingresa tu nombre: ")
apellido = input(f"Hola, {nombre}. Ahora ingresa tu apellido: ")
nombre_completo = nombre + " " + apellido
edad = input(f"{nombre_completo}, qué edad tienes? ")
residencia = input(f"Okey,{nombre_completo}, por último ingresa tu lugar de residencia: ")
print(f"{nombre_completo}, vives en {residencia} y tienes {edad} años. Mucho gusto!")

# Actividad 4: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio_circulo = float(input("Ingresa el radio de un círculo: "))
#radio_circulo = float(radio_circulo) *esta sería otra opción*
area = 3.14 * radio_circulo ** 2
perimetro = 2 * 3.14 * radio_circulo
print(f"Entonces su área es {area} y su perimetro es {perimetro}")

# Actividad 5: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Ingrese los segundos que quiera calcular: "))
horas = segundos / 3600
print(f"Entonces serían {horas}h")

# Actividad 6: Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("¡Hola! A continuación ingresa un número y recibirás la tabla de multiplicar de dicho número: "))
print("Esta es su tabla:")
print(f"{numero}x1 = {numero * 1}")
print(f"{numero}x2 = {numero * 2}")
print(f"{numero}x3 = {numero * 3}")
print(f"{numero}x4 = {numero * 4}")
print(f"{numero}x5 = {numero * 5}")
print(f"{numero}x6 = {numero * 6}")
print(f"{numero}x7 = {numero * 7}")
print(f"{numero}x8 = {numero * 8}")
print(f"{numero}x9 = {numero * 9}")
print(f"{numero}x10 = {numero * 10}")
print("Eso es todo :)")

# Actividad 7: Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("¡Hola!")
numero1 = int(input("A continuación ingresa un número entero que no sea 0: "))
numero2 = int(input("Ahora ingresa otro número entero que no sea 0: "))
print(f"{numero1} + {numero2} = {numero1 + numero2}")
print(f"{numero1} / {numero2} = {numero1 / numero2}")
print(f"{numero1} * {numero2} = {numero1 * numero2}")
print(f"{numero1} - {numero2} = {numero1 - numero2}")
print("¡Eso es todo!")

# Actividad 8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
print("¡Hola!")
print("A continuación vamos a calcular tu masa corporal.")
altura = float(input("Por favor, ingresa tu altura: "))
peso = float(input("Ahora ingresa tu peso: "))
imc = peso / (altura ** 2)
print(f"Tu masa corporal es: {imc:.2f}")

# Actividad 9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
print("Hola, amigo. Vamos a convertir grados Celsius en grados Fahrenheit.")
celsius = float(input("Ingresa tus grados Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print(f"Tus {celsius} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit")

# Actividad 10: Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
print("¡Hola! A continuación vamos a tomar 3 números y sacaremos un promedio de ellos.")
numero1 = int(input("Ingresa el primer número entero: "))
numero2 = int(input("Ingresa el segundo número entero: "))
numero3 = int(input("Ingresa el tercer número entero: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"Tu promedio es: {promedio:.2f}")
print("¡Saludos!")

# FIN DEL TRABAJO PRÁCTICO 1: Estructuras Secuenciales.