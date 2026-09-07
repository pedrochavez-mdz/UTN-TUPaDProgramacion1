# TRABAJO PRACTICO 4: Estructuras Repetitivas.
# ALUMNO: PEDRO CHÁVEZ

#Actividad 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
print("A continuación vamos a imprimir todos los números del 1 al 100.")

for i in range(1, 101):
    print(i)

print("¡Listo!")
print("=" * 20)

#Actividad 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
 # Sé que esta no es la forma correcta para este TP, pero me pareció que cumplía la función y fue más fácil.
numero = input("Ingresá un número entero positivo: ")

contador = len(numero)
if contador > 1:
    print(f"El número {numero} que ingresasate contiene {contador} digitos.")
else:
    print(f"El número {numero} que ingresasate contiene {contador} digito.")
print("=" * 20)

#Actividad 2: Es la misma consigna que la anterior pero usando bucles.
numero = input("Ingresá un número entero positivo: ")

contador = 0

while len(numero) > 0:
    contador += 1
    numero = numero[1:] 

if contador > 1:
    print(f"El número ingresado contiene {contador} dígitos.")
else:
    print(f"El número ingresado contiene {contador} dígito.")

print("=" * 20)

#Actividad 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
numero1 = int(input("Ingrese un número entero: "))
numero2 = int(input("Ingrese otro número entero y a continuación vamos a sumar todos los números comprendidos entre ambos numeros incluyendo estos: "))
elegido = 0

if numero1 < numero2:
    for i in range(numero1, numero2 + 1):
        elegido += i 
else:
    for i in range(numero1, numero2 - 1, -1):
        elegido += i

print(f"La suma de los valores entre {numero1} y {numero2} es {elegido}")
print("=" * 20)

#Actividad 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
suma = 0

print("Hola, a continuación podrás ingresar números enteros y recibir la suma de estos.")
print ("Para detener la suma y recibir el resultado debe ingresar 0.")

while True:

    producto = int(input("Ingrese sus números enteros: "))
    if producto == 0:
        break
    suma += producto

print(f"La suma de tus números es: {suma}")
print("¡Gracias!")
print("=" * 20)

#Actividad 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
numero = 4
jugando = True
intentos = 0

print("¡Hola!")
print("\nVamos a jugar un juego. Debés adivinar el número que está guardado en la caja 📦. Tenés intentos ilimitados.")
print("Una pista: El número se encuentra entre el 0 y el 9 ¡Suerte!")

while jugando:
    secreta = int(input("Ingresá el número que tenés en mente: "))
    if secreta == numero:
        jugando = False
    elif secreta <= 0 or secreta >= 9:
        print("\n❌ No era ese número. Recordá que está entre el 0 y el 9.")
    else:
        print("\n❌ No era ese número. Intentá otra vez.")
    
    intentos += 1

print("\n🎉 ¡Acertaste!")
print(f"Necesitaste {intentos} intentos para adivinar el número.")
print("=" * 20)

#Actividad 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
print("A continuación vamos a ver los números pares que están entre 100 y 0:")

for i in range(99, 0, - 1):
    if i % 2 == 0:
        print(f"{i}")

print("Listo.")
print("=" * 20)

#Actividad 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
numero = int(input("Ingrese un número entero y a continuación vamos a sumar todos los números comprendidos entre 0 y el número elegido: "))
elegido = 0

for i in range(1, numero):
    elegido += i 

print(f"La suma de los valores entre 0 y {numero} es {elegido}")
print("=" * 20)

#Actividad 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
CANTIDAD_NUMEROS = 100
contador_positivos = 0
contador_negativos = 0
contador_pares = 0
contador_impares = 0
contador = 0

for i in range(CANTIDAD_NUMEROS):
    numero = int(input("Ingrese un número y use 0 para finalizar: "))
    if numero == 0:
        break

    contador +=1
    
    if numero > 0:
        contador_positivos += 1
        if numero % 2 == 0:
                contador_pares += 1
        else:
            contador_impares += 1
    else:
        contador_negativos += 1
        if numero % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1
    
if contador > 1:
    print(f"Usted ingresó {contador} números")
else:
     print(f"Usted ingresó {contador} número")

if contador_positivos > 1:
    print(f"{contador_positivos} son números positivos.")
else:
    print(f"{contador_positivos} es un número positivo.")

if contador_negativos > 1:
    print(f"{contador_negativos} son números negativos.")
else:
    print(f"{contador_negativos} es un número negativo.")

if contador_pares > 1:
    print(f"{contador_pares} son números pares.")
else:
    print(f"{contador_pares} es un número par.")

if contador_impares > 1:
    print(f"{contador_impares} son números impares.")
else:
    print(f"{contador_impares} es un número impar.")

print("=" * 20)

#Actividad 9:  Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
CANTIDAD_NUMEROS = 100
cantidad_ingresada = 0
suma_numeros = 0

for i in range(CANTIDAD_NUMEROS):
    numero = float(input("Ingrese un número y use 0 para finalizar: "))
    if numero == 0:
        break

    cantidad_ingresada += 1
    suma_numeros += numero

if cantidad_ingresada > 0:
    media = suma_numeros / cantidad_ingresada
    print(f"El promedio es: {media:.2f}")
else:
    print("No se ingresaron números, no se puede calcular el promedio.")
print("=" * 20)

#Actividad 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = input("Ingresá un número entero positivo: ")
inverso = ""

for digito in numero:
    inverso = digito + inverso

numero_invertido = int(inverso)

print(f"El número invertido es: {numero_invertido}")
print("=" * 20)

# FIN DEL TRABAJO PRÁCTICO 4: Estructuras Repetitivas.