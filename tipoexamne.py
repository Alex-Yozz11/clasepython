print("EXAMEN DE ALEX YOZA TUMBACO :)")
print("SISTEMA DE INGRESOS DE ALUMNOS Y DE NOTAS")

# Validar cantidad de alumnos
while True:
    try:
        registro_alumnos = int(input("¿Cuántos alumnos deseas ingresar?: "))
        if registro_alumnos > 0:
            break
        else:
            print("Por favor, ingresa un número válido mayor que 0.")
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entero.")

# Listas para almacenar nombres y promedios
nombres = []
promedios = []

# Bucle principal
for i in range(registro_alumnos):
    print(f"[Alumno #{i + 1}] Ingrese el nombre:")
    nombre = input().strip()

    while not nombre:
        print("El nombre no puede estar vacío. Intenta de nuevo.")
        nombre = input(f"[Alumno #{i + 1}] Ingrese el nombre: ").strip()

    nombres.append(nombre)

    # Pedir cantidad de notas
    while True:
        try:
            cantidad_notas = int(input(f"[Alumno #{i + 1}] ¿Cuántas notas desea ingresar?: "))
            if cantidad_notas > 0:
                break
            else:
                print("Por favor, ingresa un número válido mayor que 0.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")

    # Ingresar las notas
    suma_notas = 0
    for j in range(cantidad_notas):
        while True:
            try:
                nota = float(input(f"Ingrese la nota #{j + 1}: "))
                if 0 <= nota <= 10:
                    suma_notas += nota
                    break
                else:
                    print("Nota inválida. Debe estar entre 0 y 10.")
            except ValueError:
                print("Entrada inválida. Debes ingresar un número.")

    promedio = suma_notas / cantidad_notas
    promedios.append(promedio)

# Mostrar resumen
print("\nRESUMEN DE ALUMNOS")
for i in range(registro_alumnos):
    aprobado = promedios[i] >= 7
    estado = "Aprobado" if aprobado else "Reprobado"
    print(f"{nombres[i]} - Promedio: {promedios[i]:.2f} - {estado}")

# Mostrar mejor y peor promedio
if promedios:
    promedio_maximo = max(promedios)
    promedio_minimo = min(promedios)
    indice_max = promedios.index(promedio_maximo)
    indice_min = promedios.index(promedio_minimo)
    mejor_alumno = nombres[indice_max]
    peor_alumno = nombres[indice_min]

    print(f"\nMejor promedio: {mejor_alumno} ({promedio_maximo:.2f})")
    print(f"Peor promedio: {peor_alumno} ({promedio_minimo:.2f})")
    print("FIN DEL EXAMENNNNNNNNNN")

