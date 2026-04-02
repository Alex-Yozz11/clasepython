print("Actividad en pareja: Alex Yoza y Vivian Moran")

"""
Programa que calcula el salario de un profesor con incremento anual.

Se calcula el salario durante 6 años aplicando un incremento del 10%.
Se muestra el salario de cada año y el salario final.
"""

print("Programa para calcular el salario anual de un empleado con un incremento del 10% durante 6 años.")


def calcular_salarios(salario_inicial, incremento_anual, total_anios):
    """
    Calcula los salarios año por año.

    Parámetros:
        salario_inicial (float): Salario base inicial.
        incremento_anual (float): Incremento anual en formato decimal.
        total_anios (int): Número de años a calcular.

    Retorna:
        list: Lista con los salarios de cada año.
    """
    salarios = []
    salario_actual = salario_inicial
    contador = 1

    while contador <= total_anios:
        salarios.append(salario_actual)
        salario_actual = salario_actual * (1 + incremento_anual)
        contador += 1

    return salarios

  
def mostrar_resultados(lista_salarios):
    """
    Muestra los salarios por año y el salario final.

    Parámetros:
        lista_salarios (list): Lista de salarios calculados.

    Retorna:
        None
    """
    indice = 0

    while indice < len(lista_salarios):
        print(f"Año {indice + 1}: ${lista_salarios[indice]:.2f}")
        indice += 1

    print(
        f"Salario final después de {len(lista_salarios)} años: "
        f"${lista_salarios[-1]:.2f}"
    )

  
def main():
    """
    Función principal que ejecuta el programa.

    Retorna:
        None
    """
    salario_inicial = 1500.0
    incremento_anual = 0.10
    total_anios = 6

    salarios = calcular_salarios(
        salario_inicial,
        incremento_anual,
        total_anios
    )

    mostrar_resultados(salarios)


if __name__ == "__main__":
    main()