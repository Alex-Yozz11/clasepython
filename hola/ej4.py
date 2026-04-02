"""
Módulo de Gestión de Viajes de Transporte.
Clasifica viajes por kilometraje y acumula distancias recorridas.
"""

def clasificar_viajes(distancias):
    """
    Agrupa los viajes en categorías según la distancia recorrida.

    Args:
        distancias (list): Distancias de los viajes en kilómetros.

    Returns:
        dict: Diccionario estructurado con conteos y totales por categoría.

    Example:
        >>> clasificar_viajes([3.5, 10.0, 20.2])
        {'cortos': (1, 3.5), 'medios': (1, 10.0), 'largos': (1, 20.2), ...}
    """
    c_cor, t_cor = 0, 0.0
    c_med, t_med = 0, 0.0
    c_lar, t_lar = 0, 0.0

    for dist in distancias:
        if dist <= 5:
            c_cor += 1
            t_cor += dist
        elif dist <= 15:
            c_med += 1
            t_med += dist
        else:
            c_lar += 1
            t_lar += dist

    return {
        "cortos": (c_cor, t_cor),
        "medios": (c_med, t_med),
        "largos": (c_lar, t_lar),
        "distancia_total": sum(distancias)
    }

def main():
    """Función de entrada para procesar la jornada del conductor."""
    print("--- RESUMEN DE JORNADA ---")
    try:
        n_viajes = int(input("Ingrese el número total de viajes de hoy: "))
        viajes = [
            float(input(f"Distancia viaje {i+1} (km): ")) for i in range(n_viajes)
        ]
        
        datos = clasificar_viajes(viajes)
        
        print("\n--- REPORTE DE VIAJES ---")
        print(f"Viajes Cortos : {datos['cortos'][0]} | Total: {datos['cortos'][1]} km")
        print(f"Viajes Medios : {datos['medios'][0]} | Total: {datos['medios'][1]} km")
        print(f"Viajes Largos : {datos['largos'][0]} | Total: {datos['largos'][1]} km")
        print(f"DISTANCIA GLOBAL: {datos['distancia_total']:.2f} km")
    except ValueError:
        print("Por favor, ingrese valores numéricos.")

if __name__ == "__main__":
    main()