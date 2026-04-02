"""
Módulo de Evaluación de Calificaciones.
Clasifica notas de estudiantes y calcula el promedio general del grupo.
"""

def evaluar_notas(notas):
    """
    Clasifica las calificaciones y calcula promedios.

    Args:
        notas (list): Lista de calificaciones de los estudiantes (float).

    Returns:
        dict: Conteo y suma por cada nivel de calificación, y promedio.

    Example:
        >>> evaluar_notas([95.0, 75.0, 50.0])
        {'excelente': (1, 95.0), 'promedio_general': 73.33, ...}
    """
    if not notas:
        return None

    c_exc, t_exc = 0, 0.0
    c_apr, t_apr = 0, 0.0
    c_rep, t_rep = 0, 0.0

    for nota in notas:
        if nota >= 90:
            c_exc += 1
            t_exc += nota
        elif nota >= 70:
            c_apr += 1
            t_apr += nota
        else:
            c_rep += 1
            t_rep += nota

    promedio = sum(notas) / len(notas)

    return {
        "excelente": (c_exc, t_exc),
        "aprobado": (c_apr, t_apr),
        "reprobado": (c_rep, t_rep),
        "promedio_general": promedio
    }

def main():
    """Ejecuta el programa de evaluación de notas interactivo."""
    print("--- SISTEMA DE CALIFICACIONES ---")
    try:
        n_notas = int(input("Ingrese cantidad de estudiantes: "))
        lista_notas = [
            float(input(f"Nota estudiante {i+1}: ")) for i in range(n_notas)
        ]
        
        datos = evaluar_notas(lista_notas)
        
        print("\n--- REPORTE ACADÉMICO ---")
        print(f"Excelentes: {datos['excelente'][0]} (Suma: {datos['excelente'][1]})")
        print(f"Aprobados: {datos['aprobado'][0]} (Suma: {datos['aprobado'][1]})")
        print(f"Reprobados: {datos['reprobado'][0]} (Suma: {datos['reprobado'][1]})")
        print(f"Promedio del Grupo: {datos['promedio_general']:.2f}")
    except ValueError:
        print("Error en el ingreso de datos.")

if __name__ == "__main__":
    main()