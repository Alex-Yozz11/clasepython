"""
Módulo de Análisis de Consumo Eléctrico.
Clasifica electrodomésticos por consumo en Watts y calcula totales.
"""

def analizar_consumo(lista_watts):
    """
    Clasifica los consumos eléctricos y totaliza por categoría.

    Args:
        lista_watts (list): Consumos de los electrodomésticos en Watts.

    Returns:
        dict: Conteo y total de Watts por categoría, y total global.

    Example:
        >>> analizar_consumo([150.0, 800.0, 1500.0])
        {'bajo': (1, 150.0), 'medio': (1, 800.0), 'alto': (1, 1500.0), ...}
    """
    cat_bajo = {"conteo": 0, "total": 0.0}
    cat_medio = {"conteo": 0, "total": 0.0}
    cat_alto = {"conteo": 0, "total": 0.0}

    for watt in lista_watts:
        if watt < 300:
            cat_bajo["conteo"] += 1
            cat_bajo["total"] += watt
        elif watt <= 1000:
            cat_medio["conteo"] += 1
            cat_medio["total"] += watt
        else:
            cat_alto["conteo"] += 1
            cat_alto["total"] += watt

    return {
        "bajo": cat_bajo,
        "medio": cat_medio,
        "alto": cat_alto,
        "consumo_global": sum(lista_watts)
    }

def main():
    """Función para el registro y reporte de consumo."""
    print("--- ANÁLISIS ELÉCTRICO ---")
    try:
        n = int(input("¿Cuántos electrodomésticos evaluará?: "))
        watts = [
            float(input(f"Consumo equipo {i+1} (Watts): ")) for i in range(n)
        ]
        
        res = analizar_consumo(watts)
        
        print("\n--- REPORTE DE CONSUMO ---")
        for clave in ["bajo", "medio", "alto"]:
            conteo = res[clave]["conteo"]
            total = res[clave]["total"]
            print(f"Equipos de consumo {clave}: {conteo} (Total: {total}W)")
            
        print("-" * 30)
        print(f"CONSUMO TOTAL DE LA CASA: {res['consumo_global']}W")
    except ValueError:
        print("Entrada inválida. Use solo números.")

if __name__ == "__main__":
    main()