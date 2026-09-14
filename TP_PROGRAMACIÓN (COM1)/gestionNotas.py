alumnos = {60902: "Rodolfo Fernandez", 61654: "Luis Gomez", 61852: "Andrea Pereira", 61754: "Juan Cruz Gonzales"}
materias = [
    ["Ciencias", 0, 0, 0],
    ["Historia", 0, 0, 0],
    ["Geografía", 0, 0, 0],
    ["Matemáticas", 0, 0, 0],
    ["Física", 0, 0, 0]
]
notasFinales = []

for legajo, nombre in alumnos.items():
    print(f"Ingrese las notas del alumno {nombre}(Legajo - {legajo})")
    notasAlumno = {}
    for materia in materias:
        print(f"Ingrese las notas para la materia {materia[0]}")
        nota1= float(input("Nota 1: "))
        while nota1 < 0 or nota1 > 10:
            print("La nota debe estar entre 0 y 10.")
            nota1 = float(input("Nota 1: "))
        nota2= float(input("Nota 2: "))
        while nota2 < 0 or nota2 > 10:
            print("La nota debe estar entre 0 y 10.")
            nota2 = float(input("Nota 2: "))
        materia[1] = nota1
        materia[2] = nota2 
        promedio = (nota1 + nota2) / 2
        materia[3] = promedio
        print(f"Nota final: {materia[3]}")
        notasAlumno[materia[0]] = promedio
    nota_alta = -1
    materia_alta = ""
    suma_promedio = 0

    for mat, nota in notasAlumno.items():
        suma_promedio += nota
        if nota > nota_alta:
            nota_alta = nota
            materia_alta = mat
    promedio_general = suma_promedio / len(notasAlumno)
    notasFinales.append([nombre,promedio_general])
    print(f"Informe de {nombre}.")
    print(f"Materia con nota más alta: {materia_alta} ({nota_alta})")
    print(f"Promedio general: {promedio_general:.2f}")

mejorPromedio = -1
mejorAlumno = ""
for alumno in notasFinales:
    if alumno[1] > mejorPromedio:
        mejorPromedio = alumno[1]
        mejorAlumno = alumno[0]
print(f"El alumno con el mejor promedio general es {mejorAlumno} con {mejorPromedio:.2f}")        
    
