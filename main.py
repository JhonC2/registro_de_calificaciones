# Diccionario vacío para agregar a todos los estudiantes.
lista_de_calificaciones = {}

print("Bienvenido al registro de calificaciones del periodo 2026-2027")
    
# Bucle infinito para agregar, actualizar o salir del registro de calificaciones
while True:
    print("Elija una opción:")
    print("1.- Agregar estudiante.")
    print("2.- Actualizar nota del estudiante.")
    print("3.- Salir del registro de calificaciones.")
    
    user = int(input("Ingresa una opción (1-3): "))
    
    if user == 1:
        estudiante = input("Ingresa el nombre del estudiante: ")
        nota = float(input(f"Ingresa la nota de {estudiante}: "))
        
        if nota != "":
            lista_de_calificaciones[estudiante] = nota
            print("Estudiante agregado exitosamente.\n")
    elif user == 2:
        if estudiante in lista_de_calificaciones:
            lista_de_calificaciones[estudiante] = nota
    elif user == 3:
        print("Salida exitosa. Hasta pronto!\n")
        break
    else:
        print("Opción incorrecta. Ingresa una opción entre (1-3).")

# Recorrer la lista de calificaciones para imprimir el nombre del estudiante y su nota.
print("Registro de calificaciones")
for estudiante, nota in lista_de_calificaciones.items():
    print(f"{estudiante}: {nota:.2f}")

# Calcular la media de las notas
calificaciones = lista_de_calificaciones.values()

media = sum(calificaciones) / len(calificaciones)

print("\nNota media:")
print(f"La nota media de las calificaciones es: {media:.2f}\n")

# Obtener la nota maxima y minima
nota_maxima = max(calificaciones)

nota_minima = min(calificaciones)

print("Nota maxima y minimo del registro de calificaciones: ")
print(f"Nota maxima: {nota_maxima:.2f}")
print(f"Nota minima: {nota_minima:.2f}\n")

# Calcular si un estudiante aprobó o reprobó la asignatura

print("Estudiantes Aprobados y Reprobados:")
for estudiante, nota in lista_de_calificaciones.items():
    if nota >= 7:
        print(f"{estudiante}: {nota} - 'Aprobado'")
    else:
        print(f"{estudiante}: {nota} - 'Reprobado'")