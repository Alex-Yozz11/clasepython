"""
Nombre: Alex Yoza Tumbaco
Programa de conteo numérico - Versión alternativa - Examen 
Este script clasifica números ingresados por el usuario entre positivos y no positivos.
"""

def pedir_cantidad():
    """Solicita el total de números a procesar con control de errores"""
    while True:
        try:
            total = input("¿Cuántos números deseas analizar: ? ")
            total = int(total)
            if total < 1:
                print("ERROR El valor debe ser 1 o más.")
                continue
            return total
        except:
            print("Entrada inválida. Escriba un número entero positivo.")

def capturar_datos(cuenta):
    """Recolecta los números uno por uno"""
    lista_completa = []
    contador = 1
    while contador <= cuenta:
        try:
            dato = input(f"Número #{contador}: ")
            valor_num = float(dato)
            lista_completa.append(valor_num)
            contador += 1
        except:
            print("Valor incorrecto. Ingrese un número (ej: 3, -1.5, 0)")
    return lista_completa

def clasificar(numeros_recibidos):
    """Separa en dos grupos: cero/negativos y positivos"""
    no_positivos = 0
    positivos = 0
   
    for elemento in numeros_recibidos:
        if elemento > 0:
            positivos = positivos + 1
        else:
            no_positivos = no_positivos + 1
           
    return no_positivos, positivos

def mostrar_informe(menores_iguales, mayores):
    """Imprime el resultado final"""
    print("\n" + "="*35)
    print(" *** RESULTADO *** ")
    print("="*35)
    print(f"* Números ≤ 0 ............: {menores_iguales}")
    print(f"* Números > 0 ............: {mayores}")
    print("="*35)

def arrancar():
    """Función principal que inicia todo"""
    print("")
    print(">>> SISTEMA DE CLASIFICACIÓN NUMÉRICA <<<")
    print("")
   
    cantidad = pedir_cantidad()
    datos_usuario = capturar_datos(cantidad)
    cont_cero_neg, cont_pos = clasificar(datos_usuario)
    mostrar_informe(cont_cero_neg, cont_pos)
   
    print("\n¡Análisis completado!")

if __name__ == "__main__":
    arrancar()