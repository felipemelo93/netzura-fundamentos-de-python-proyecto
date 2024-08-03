def solicitar_datos_alumnos():
    # Solicitar la cantidad de alumnos
    N = int(input("Ingrese la cantidad de alumnos: "))

    for i in range(N):
        # Solicitar la cantidad de notas
        M = int(input(f"\nIngrese la cantidad de notas para el alumno {i + 1}: "))
        
        # Solicitar nombre, apellido, sección y grado
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        seccion = input("Ingrese la sección del alumno: ")
        grado = input("Ingrese el grado del alumno: ")
        
        # Inicializar lista para almacenar notas
        notas = []

        for j in range(M):
            while True:
                nota = float(input(f"Ingrese la nota {j + 1} (debe estar entre 0 y 20): "))
                if 0 <= nota <= 20:
                    notas.append(nota)
                    break
                else:
                    print("El valor de la nota no pertenece a un rango válido. Intente nuevamente.")
        
        # Calcular promedio de notas
        promedio = sum(notas) / M

        # Mostrar promedio y mensaje de aprobación o desaprobación
        print(f"\nPromedio de notas del alumno {nombre} {apellido}: {promedio:.2f}")
        if promedio < 10.5:
            print("Ha desaprobado el curso")
        else:
            print("Felicitaciones, aprobó el curso")
        
        # Mostrar nota mayor y nota menor
        print(f"Nota mayor: {max(notas)}")
        print(f"Nota menor: {min(notas)}")

# Llamar a la función para ejecutar el programa
solicitar_datos_alumnos()