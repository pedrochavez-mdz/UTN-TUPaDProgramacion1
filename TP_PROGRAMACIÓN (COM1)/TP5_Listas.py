#T.P. 5 Listas
#Alumno: Pedro Chávez (Comisión 1)

#Actividad 1
multiplos_4 = []
for i in range(4, 101, 4):
    multiplos_4.append(i)    
print(multiplos_4)
print("=" * 20)

#Actividad 2
lista_elementos = ["Mendoza", "azul", "verde", "arbol", "pelota"]
print(lista_elementos[3])
print("=" * 20)

#Actividad 3
lista_vacia = []
lista_vacia.append("Práctico")
lista_vacia.append("de")
lista_vacia.append("Programación")
print(lista_vacia)
print("=" * 20)

#Actividad 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"
print(animales)
print("=" * 20)

#Actividad 5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
print("En este programa se busca el valor más alto de la lista con max y se elimina con remove.")
print("=" * 20)

#Actividad 6
lista_numeros = []
for i in range(10, 31, 5):
    lista_numeros.append(i)
print(lista_numeros[0], lista_numeros[1])
print("=" * 20)

#Actividad 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "cronos"
autos[2] = "amarok"
print(autos) 
print("=" * 20)

#Actividad 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)
print("=" * 20)

#Actividad 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)
print("=" * 20)

#Actividad 10
lista_anidada = [15, True,[25.5, 57.9, 30.6], False]
print(lista_anidada)

#FIN