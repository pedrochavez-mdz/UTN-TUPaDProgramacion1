#TP6: Funciones
#Alumno: Pedro Chávez(Comisión 1)
#ACTIVIDAD 1
def imprimir_hola_mundo ():
    print("Hola, Mundo!")

if __name__ == "__main__":
    imprimir_hola_mundo()
print("=" * 20)

#ACTIVIDAD 2
def saludar_usuario(nombre):
    return f"Hola, {nombre}!"
if __name__ == "__main__":
    nombre_ingresado = input("Su nombre: ")
    mensaje = saludar_usuario(nombre_ingresado)
    print(mensaje)
print("=" * 20)

#ACTIVIDAD 3
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."
if __name__ == "__main__":
    nombre_1 = input("Ingrese nombre: ")
    apellido_1 = input("Ingrese apellido: ")
    edad_1 = int(input("Ingrese edad: "))
    residencia_1 = input("Ingrese residencia: ")
    soy = informacion_personal(nombre_1, apellido_1, edad_1, residencia_1)
    print(soy) 
print("=" * 20)

#ACTIVIDAD 4
def calcular_area_circulo(radio):
    area = round(3.14 * radio ** 2)
    return area
def calcular_perimetro_circulo(radio):
    perimetro = round(2 * 3.14 * radio)
    return perimetro
if __name__ == "__main__":
    radio = float(input("Ingrese un radio: "))
    calculo_area = calcular_area_circulo(radio)
    calculo_perimetro = calcular_perimetro_circulo(radio)
    print(f"Área: {calculo_area}")
    print(f"Perímetro: {calculo_perimetro}")
print("=" * 20)

#ACTIVIDAD 5
def segundos_a_horas(segundos):
    convierte_seg = segundos / 3600
    return convierte_seg
if __name__ == "__main__":
    segundos = float(input("Ingrese segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos}seg. = {horas}h.")
print("=" * 20)

#ACTIVIDAD 6
def tabla_multiplicar(numero):
   for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
if __name__ == "__main__":
    numero = int(input("Ingrese un número entero: "))
    tabla_multiplicar(numero)
print("=" * 20)

#ACTIVIDAD 7
def operaciones_basicas(a, b):
   operaciones = (a + b, a - b, a* b, a/ b)
   return operaciones
if __name__ == "__main__":
    numero1 = int(input("Ingrese un número entero: "))
    numero2 = int(input("Ingrese otro número entero: "))
    resultado = operaciones_basicas(numero1, numero2)
    print(f"{numero1} + {numero2} = {resultado[0]}")
    print(f"{numero1} - {numero2} = {resultado[1]}")
    print(f"{numero1} * {numero2} = {resultado[2]}")
    print(f"{numero1} / {numero2} = {resultado[3]}")
print("=" * 20)

#ACTIVIDAD 8
def calcular_imc(peso, altura):
    calculo_imc = (peso / altura ** 2)
    return calculo_imc
if __name__ == "__main__":
    peso_i = float(input("Ingrese su peso: "))
    altura_i = float(input("Ingrese su altura: "))
    imc = calcular_imc(peso_i, altura_i)
    print(f"Su IMC es: {imc:.2f}")    
print("=" * 20)

#ACTIVIDAD 9
def celsius_a_fahrenheit(celsius):
    conversion = celsius * 1.8 + 32
    return conversion
if __name__ == "__main__":
    gc = float(input("Ingrese sus grados celsius: "))
    fahr = celsius_a_fahrenheit(gc)
    print(f"Sus {gc} grados Celsius equivalen a {fahr} grados Fahrenheit.")
print("=" * 20)

#ACTIVIDAD 10
def calcular_promedio(a, b, c):
    calculo = (a + b + c) / 3
    return calculo
if __name__ == "__main__":
    a = float(input("Ingrese un número: "))
    b = float(input("Ingrese un número: "))
    c = float(input("Ingrese un número: "))
    promedio = calcular_promedio(a, b, c)
    print(f"El promedio de los números es {promedio}")
#Fin