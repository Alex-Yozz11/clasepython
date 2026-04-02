"""
Módulo de Control de Calidad de Piezas.
Clasifica piezas fabricadas según su peso y calcula los totales.
"""

def clasificar_piezas(pesos):
    """
    Analiza una lista de pesos y clasifica las piezas en categorías.

    Args:
        pesos (list): Lista de pesos de las piezas en kilogramos (float).

    Returns:
        dict: Diccionario con el conteo y suma de pesos por categoría,
              y el peso total global.

    Example:
        >>> clasificar_piezas([8.5, 15.0, 22.5])
        {'ligeras': (1, 8.5), 'optimas': (1, 15.0), 'pesadas': (1, 22.5), ...}
    """
    c_lig, t_lig = 0, 0.0
    c_opt, t_opt = 0, 0.0
    c_pes, t_pes = 0, 0.0

    for peso in pesos:
        if peso < 10:
            c_lig += 1
            t_lig += peso
        elif peso <= 20:
            c_opt += 1
            t_opt += peso
        else:
            c_pes += 1
            t_pes += peso

    return {
        "ligeras": (c_lig, t_lig),
        "optimas": (c_opt, t_opt),
        "pesadas": (c_pes, t_pes),
        "total_global": sum(pesos)
    }

def main():
    """Función principal para coordinar la entrada y salida de datos."""
    print("--- CONTROL DE CALIDAD ---")
    try:
        n = int(input("Ingrese la cantidad de piezas evaluadas: "))
        lista_pesos = [
            float(input(f"Peso de la pieza {i+1} (kg): ")) for i in range(n)
        ]
        
        resultados = clasificar_piezas(lista_pesos)
        
        print("\n--- REPORTE DE PRODUCCIÓN ---")
        for cat, (cant, total) in resultados.items():
            if cat != "total_global":
                print(f"Categoría {cat.upper()}: {cant} piezas, Total: {total:.2f} kg")
        print(f"Peso Global: {resultados['total_global']:.2f} kg")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()