def clasificar_ventas(cantidad_ventas):
    """
    Clasifica las ventas en tres categorías:
    - Mayores a 1000
    - Mayores a 500 y menores o iguales a 1000
    - Menores o iguales a 500

    También calcula el monto total por categoría y el total global.

    :param cantidad_ventas: int, número total de ventas a registrar
    :return: dict, resultados de las clasificaciones y montos
    """
    mayores_1000 = 0
    entre_500_1000 = 0
    menores_500 = 0

    suma_mayores_1000 = 0.0
    suma_entre_500_1000 = 0.0
    suma_menores_500 = 0.0

    total_global = 0.0

    for i in range(cantidad_ventas):
        venta = float(input(f"Ingrese el monto de la venta #{i + 1}: "))
        total_global += venta

        if venta > 1000:
            mayores_1000 += 1
            suma_mayores_1000 += venta
        elif 500 < venta <= 1000:
            entre_500_1000 += 1
            suma_entre_500_1000 += venta
        else:
            menores_500 += 1
            suma_menores_500 += venta

    return {
        "mayores_1000": mayores_1000,
        "suma_mayores_1000": suma_mayores_1000,
        "entre_500_1000": entre_500_1000,
        "suma_entre_500_1000": suma_entre_500_1000,
        "menores_500": menores_500,
        "suma_menores_500": suma_menores_500,
        "total_global": total_global
    }


def mostrar_resultados(resultados):
    """
    Muestra en consola los resultados de las ventas clasificadas.

    :param resultados: dict, datos retornados por clasificar_ventas
    """
    print("\n--- RESULTADOS ---")
    print(f"Ventas > 1000: {resultados['mayores_1000']}")
    print(f"Monto > 1000: {resultados['suma_mayores_1000']:.2f}")

    print(f"Ventas entre 500 y 1000: {resultados['entre_500_1000']}")
    print(f"Monto entre 500 y 1000: "
          f"{resultados['suma_entre_500_1000']:.2f}")

    print(f"Ventas <= 500: {resultados['menores_500']}")
    print(f"Monto <= 500: {resultados['suma_menores_500']:.2f}")

    print(f"Monto total vendido: {resultados['total_global']:.2f}")

def main():
    """
    Función principal del programa.
    Solicita la cantidad de ventas y ejecuta el proceso completo.
    """
    try:
        cantidad = int(input("Ingrese la cantidad de ventas: "))
        if cantidad <= 0:
            print("Debe ingresar un número mayor a 0.")
            return

        resultados = clasificar_ventas(cantidad)
        mostrar_resultados(resultados)

    except ValueError:
        print("Error: Debe ingresar un número válido.")


if __name__ == "__main__":
    main()
